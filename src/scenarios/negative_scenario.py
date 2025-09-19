import requests.exceptions
from src.data_models.task_model import Task
from src.api_clients.api_task import TaskApiClient
from src.utils.response_validator import validate_response


class TaskNegativeScenarios:
    def __init__(self, task_api_client: TaskApiClient):
        self.task_api_client = task_api_client


    def create_task_with_invalid_payload(self, list_id, invalid_task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий:
        1) Попытка создать task с невалидным полем.
        2) Проверка status code. Если API не позволяет создать task с невалидным полем.
           Возвращает сообщение об ошибке.
        3) Проверка пустого значения в поле. Если API позволяет создать task с невалидным полем.
        Возвращает: сообщение json.
        """
        try:
            response = self.task_api_client.create_task_with_dict(list_id, invalid_task_payload)
            status_code = response.status_code

        except requests.exceptions.HTTPError as e:
            error_message = e.response
            assert error_message.status_code == 400, f"Expected status code 400."
            print(f"\nReceived error message: {error_message}.")
            print(f"✅ Task didn't created\n")
            return error_message.json()

        if status_code in (201, 200):
            task_id = response.json()["id"]
            created_task = self.task_api_client.get_task(task_id).json()

            for field in invalid_task_payload.keys():
                if field != "name" and field in created_task:
                    value = created_task[field]
                    assert value in (None, "", []), f"Field {field} isn't empty: {created_task[field]}."
                    print(f"\nTask send: {invalid_task_payload}.")
                    print(f"✅ Received field: {field}, value: {value}\n")

                if field == "fake_field":
                    assert field not in created_task, f"Unexpected field {field} found in created_task: {created_task}."
                    print(f"\n✅ The fake_field was not found in the task\n")

        return response.json()


    def get_non_existent_task(self, list_id ,non_existent_task_id):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий:
        1) Попытка получение несуществующего task по фейковому task_id.
        2) Проверка отсутствия таска в list.
        Возвращает: сообщение об ошибке.
        """
        try:
            self.task_api_client.get_task(non_existent_task_id)

        except requests.exceptions.HTTPError as e:
            error_message = e.response
            assert error_message.status_code == 401, f"Expected status code 401."
            print(f"\n✅ Received error message: {error_message}.")

            list_tasks = self.task_api_client.get_tasks(list_id).json()
            task_ids = [task["id"] for task in list_tasks["tasks"]]
            assert non_existent_task_id not in task_ids, f"Non existent task is in the list."
            print(f"✅ The task with the fake ID - {non_existent_task_id} is missing from the task list\n")

            return error_message.json()


    def delete_non_existent_task(self, non_existent_task_id):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий: Удаление несуществующего task.
        Возвращает: сообщение об ошибке.
        """
        try:
            self.task_api_client.delete_task(non_existent_task_id)

        except requests.exceptions.HTTPError as e:
            error_message = e.response
            assert error_message.status_code == 401, f"Expected status code 401."
            print(f"\nReceived error message: {error_message}")
            print(f"✅ The non-existent task was not removed because the task was not found\n")
            return error_message.json()


    def delete_twice_task(self, list_id, task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий:
        1) Создать task.
        2) Удалить task.
        3) Попытка повторного удаления task
        Возвращает: сообщение об ошибке.
        """
        task_id = self.task_api_client.create_task(list_id, task_payload).json()["id"]
        self.task_api_client.delete_task(task_id)

        list_tasks = self.task_api_client.get_tasks(list_id).json()
        task_ids = [task["id"] for task in list_tasks["tasks"]]
        assert task_id not in task_ids, f"Task - {task_id} was not delete"

        response = self.task_api_client.delete_task(task_id)
        assert response.status_code == 204, f"Expected status code 204"
        print(f"\n✅ Second delete returned {response.status_code}, task - {task_id} is already deleted\n")


    def create_and_update_task_with_invalid_payload(self, list_id, invalid_task_payload, default_task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий:
        1) Создать task с валидными данными
        2) Попытка изменения валидных данных task на невалидные данные
        3) Проверка прежних значения в полях task
        Возвращает: сообщение об ошибке или json с данными task.
        """
        created_task = self.task_api_client.create_task(list_id, default_task_payload)
        task_id = created_task.json().get("id")
        assert task_id is not None, "Task ID not found in response"

        validate_response(
            created_task,
            model = Task,
            expected_data=default_task_payload.model_dump()
        )


        try:
            response = self.task_api_client.update_task_with_dict(list_id, invalid_task_payload)
            status_code = response.status_code

        except requests.exceptions.HTTPError as e:
            error_message = e.response
            assert error_message.status_code == 401, f"Expected status code 401."
            print(f"\nReceived error message: {error_message}.")
            print(f"\nTask send: {invalid_task_payload}.")
            print(f"✅ Task didn't updated\n")
            return error_message.json()
