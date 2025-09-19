from src.api_clients.api_task import TaskApiClient
from src.scenarios.negative_scenario import TaskNegativeScenarios


class TestNegativeTasks:


    def test_create_task_with_invalid_payload(self, auth_session, folderless_list, invalid_task_payload):
        #     5. Написать параметризованный негативный тест для Create Task
        scenario = TaskNegativeScenarios(task_api_client=TaskApiClient(auth_session))
        scenario.create_task_with_invalid_payload(folderless_list, invalid_task_payload)


    def test_get_non_existent_task(self, auth_session, folderless_list, non_existent_task_id):
        #     6. Написать негативный тест для Get Task
        scenario = TaskNegativeScenarios(task_api_client=TaskApiClient(auth_session))
        scenario.get_non_existent_task(folderless_list, non_existent_task_id)


    def test_update_with_invalid_data(self, auth_session,
                                      folderless_list, invalid_task_payload, default_task_payload):
        #   7. Написать негативный тест для Update Task
        scenario = TaskNegativeScenarios(task_api_client=TaskApiClient(auth_session))
        scenario.create_and_update_task_with_invalid_payload(folderless_list,
                                                             invalid_task_payload, default_task_payload)


    def test_delete_non_existent_task(self, auth_session, non_existent_task_id):
        #     8. Написать негативный тест для Delete Task
        scenario = TaskNegativeScenarios(task_api_client=TaskApiClient(auth_session))
        scenario.delete_non_existent_task(non_existent_task_id)


    def test_delete_twice_task(self, auth_session, folderless_list, default_task_payload):
        #     8. Написать негативный тест для Delete Task
        scenario = TaskNegativeScenarios(task_api_client=TaskApiClient(auth_session))
        scenario.delete_twice_task(folderless_list, default_task_payload)


