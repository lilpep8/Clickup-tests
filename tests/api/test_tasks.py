from src.api_clients.api_task import TaskApiClient
from src.scenarios.positive_scenario import TaskPositiveScenarios


class TestCrudTasks:

    def test_create_task(self, auth_session, folderless_list, default_task_payload):
        # 1. Написать тест для Create Task
        scenario = TaskPositiveScenarios(task_api_client=TaskApiClient(auth_session))
        task_id = scenario.create_task_and_immediately_delete(folderless_list, default_task_payload)
        assert task_id is not None


    def test_get_task(self, auth_session, folderless_list, default_task_payload ):
        # 2. Написать тест для Get Task
        scenario = TaskPositiveScenarios(task_api_client=TaskApiClient(auth_session))
        json_task = scenario.get_and_verify_task_exist(folderless_list, default_task_payload)
        assert json_task is not None


    def test_update_task(self, auth_session, folderless_list,  updated_task_payload, default_task_payload):
        # 3. Написать тест для Update Task
        scenario = TaskPositiveScenarios(task_api_client=TaskApiClient(auth_session))
        json_task = scenario.create_and_update_task(folderless_list, updated_task_payload, default_task_payload)
        assert json_task is not None


    def test_delete_task(self, auth_session, folderless_list, default_task_payload):
        # 4. Написать тест для Delete Task
        scenario = TaskPositiveScenarios(task_api_client=TaskApiClient(auth_session))
        json_task = scenario.delete_existing_task_and_verify(folderless_list, default_task_payload)
        assert json_task is None

