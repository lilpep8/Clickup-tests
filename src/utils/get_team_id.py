from src.config.api_constants import api_config


def get_team_id(self):
    """ Получение team id для создания space"""
    response = self.auth_session.get(f"{api_config.BASE_URL}/api/v2/user")
    assert response.status_code == 200, f"User data fetch failed: {response.status_code}"
    data = response.json()
    assert "teams" in data, "Response missing 'teams'"
    team_id = data["teams"][0]["id"]
    return team_id




# @pytest.fixture
# def team_id(auth_session):
#     """ Получение team id для создания space"""
#     response = auth_session.get(f"{api_config.BASE_URL}/api/v2/team")
#     assert response.status_code == 200, f"User data fetch failed: {response.status_code}"
#     data = response.json()
#     assert "teams" in data, "Response missing 'teams'"
#     return data["teams"][0]["id"]