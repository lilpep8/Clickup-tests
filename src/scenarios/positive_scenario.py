from src.api_clients.api_task import TaskApiClient
from src.data_models.task_model import Task
from src.utils.response_validator import validate_response


class TaskPositiveScenarios:
    def __init__(self, task_api_client: TaskApiClient):
        self.task_api_client = task_api_client


    def create_task_and_immediately_delete(self, list_id, default_task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий: создать task, валидировать ответ и сразу же его удалить.
        Возвращает ID созданного и удаленного task.
        """
        created_task = self.task_api_client.create_task(list_id, default_task_payload)
        task_id = created_task.json().get("id")
        assert task_id is not None, "Task ID not found in response"

        validate_response(
            created_task,
            model = Task,
            expected_data=default_task_payload.model_dump()
        )

        print(f"\n✅ Creating task was success - {task_id}")
        assert task_id is not None, "Task was not actually created"
        self.task_api_client.delete_task(task_id)
        print(f"✅ Task was deleted - {task_id}\n")
        return task_id


    def get_and_verify_task_exist(self, list_id, default_task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий: создать task, получить task и убедиться что он не пуст.
        Возвращает task.
        """
        created_task = self.task_api_client.create_task(list_id, default_task_payload)
        task_id = created_task.json().get("id")
        task = self.task_api_client.get_task(task_id)
        print(f"\n✅ Task extraction completed successfully - {task_id}\n")
        return task


    def create_and_update_task(self, list_id, updated_task_payload, default_task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий: создать task, изменить task и убедиться, что данные изменились.
        Возвращает id task.
        """
        created_task = self.task_api_client.create_task(list_id, default_task_payload)
        task_id = created_task.json().get("id")
        assert task_id is not None, "Task ID not found in response"

        validate_response(
            created_task,
            model = Task,
            expected_data=default_task_payload.model_dump()
        )

        updated_task = self.task_api_client.update_task(task_id, updated_task_payload)

        validate_response(
            updated_task,
            model = Task,
            expected_data=updated_task_payload.model_dump()
        )

        updated_task_json = updated_task.json()
        assert updated_task_json["name"] != default_task_payload.name , f"Task wasn't updated"
        print(f"\n✅ Task updated successfully - {task_id}\n")
        return task_id


    def delete_existing_task_and_verify(self, list_id, default_task_payload):
        """
        Предварительно создание space и list упаковано в фикстуры.
        Сценарий: создать task, удалить task и убедиться, что он удален.
        Возвращает None.
        """
        created_task = self.task_api_client.create_task(list_id, default_task_payload)
        task_id = created_task.json().get("id")
        response = self.task_api_client.delete_task(task_id)
        assert response.status_code == 204, f"Deleting wasn't success f{response.status_code}"
        print(f"\n✅ Task was deleted - {task_id}\n")
        return None
