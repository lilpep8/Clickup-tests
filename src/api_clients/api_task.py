from src.config.api_constants import api_config


class TaskApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config.BASE_URL


    def create_task(self, list_id: int, task_payload):
        # https://api.clickup.com/api/v2/list/{list_id}/task
        """
        :param list_id: int
        :param task_payload: model_dump
        :return: response
        """
        response = self.auth_session.post(f"{self.base_url}/api/v2/list/{list_id}/task", json = task_payload.model_dump())
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response


    def delete_task(self, task_id: int):
        # https://api.clickup.com/api/v2/task/{task_id}
        """
        :param task_id: int
        :return: response
        """
        response = self.auth_session.delete(f"{self.base_url}/api/v2/task/{task_id}")
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response


    def get_task(self, task_id: int):
        # https://api.clickup.com/api/v2/task/{task_id}
        """
        :param task_id: int
        :return: response
        """
        response = self.auth_session.get(f"{self.base_url}/api/v2/task/{task_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response


    def update_task(self, task_id: int, updated_payload):
        # https://api.clickup.com/api/v2/task/{task_id}
        """
        :param task_id: int
        :param updated_payload: model_dump
        :return: response
        """
        response = self.auth_session.put(f"{self.base_url}/api/v2/task/{task_id}", json = updated_payload.model_dump(exclude_none=True))
        if response.status_code != 200:
            response.raise_for_status()
        return response


    def get_tasks(self, list_id):
        # https://api.clickup.com/api/v2/list/{list_id}/task
        """
        :param list_id: int
        :return: response
        """
        response = self.auth_session.get(f"{self.base_url}/api/v2/list/{list_id}/task")
        if response.status_code != 200:
            response.raise_for_status()
        return response


    def create_task_with_dict(self, list_id: int, task_payload: dict):
        """
        :param list_id: int
        :param task_payload: dict
        :return: response
        """
        response = self.auth_session.post(f"{self.base_url}/api/v2/list/{list_id}/task", json = task_payload)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        return response


    def update_task_with_dict(self, list_id: int, updated_payload: dict):
        # https://api.clickup.com/api/v2/task/{task_id}
        """
        :param list_id: int
        :param updated_payload: dict
        :return: response
        """
        response = self.auth_session.put(f"{self.base_url}/api/v2/task/{list_id}", json = updated_payload)
        if response.status_code != 200:
            response.raise_for_status()
        return response