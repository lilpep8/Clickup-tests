from src.config.api_constants import api_config
from src.api_clients.api_space import SpaceApiClient


class ListApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = api_config.BASE_URL


    def create_folderless_list(self, space_id, list_payload):
        # https://api.clickup.com/api/v2/space/{space_id}/list
        """Создание листа для тасок.
           Принимает space_id и list_payload.
           Возвращает list_id
        """
        response = self.auth_session.post(f"{self.base_url}/api/v2/space/{space_id}/list", json = list_payload)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()["id"]


    def delete_list(self, list_id):
        # https://api.clickup.com/api/v2/list/{list_id}
        """Удаляет лист.
           Принимает list_id.
           Возвращает status_code
        """
        response = self.auth_session.delete(f"{self.base_url}/api/v2/list/{list_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response.status_code
