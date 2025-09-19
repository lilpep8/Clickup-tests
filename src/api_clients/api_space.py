from src.config.api_constants import api_config


class SpaceApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config.BASE_URL


    def create_space(self, team_id, space_payload):
        # https://api.clickup.com/api/v2/team/{team_id}/space
        """ Создает space для листов и тасок.
            Принимает team_id(Path Params) для base url.
            Также принимает name, multiple_assignees, features.(Body Params)

            Возвращает space id.
        """
        response = self.auth_session.post(f"{self.base_url}/api/v2/team/{team_id}/space", json = space_payload)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()["id"]


    def delete_space(self, space_id):
        # https://api.clickup.com/api/v2/space/{space_id}
        """ Удаляет пространство для листов и тасок.
            Принимает space_id.
            Возвращает id.
        """
        response = self.auth_session.delete(f"{self.base_url}/api/v2/space/{space_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response.status_code
