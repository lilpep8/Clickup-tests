import requests
import pytest
import random
import string

from faker import Faker
from src.api_clients.api_list import ListApiClient
from src.api_clients.api_space import SpaceApiClient
from src.config.api_constants import api_config
from src.data_models.task_model import Task


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    # Добавляем заголовки с токеном
    session.headers.update({
        "Authorization": api_config.AUTH_DATA.get("Authorization", ""),
        "accept": "application/json"
    })

    # Пробный запрос на проверку авторизации
    response = session.get(f"{api_config.BASE_URL}/api/v2/user")
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"
    return session


@pytest.fixture(scope="class")
def team_id(auth_session):
    """ Получение team id для создания space"""
    response = auth_session.get(f"{api_config.BASE_URL}/api/v2/team")
    assert response.status_code == 200, f"User data fetch failed: {response.status_code}"
    data = response.json()
    assert "teams" in data, "Response missing 'teams'"
    return data["teams"][0]["id"]


@pytest.fixture(scope="class")
def space(auth_session, team_id):
    client = SpaceApiClient(auth_session)
    space_payload = {
        "multiple_assignees": True,
        "features": {
            "due_dates": {
                "enabled": True,
                "start_date": True,
                "remap_due_dates": True,
                "remap_closed_due_date": True
            },
            "time_tracking": {"enabled": True},
            "tags": {"enabled": True},
            "time_estimates": {"enabled": True},
            "checklists": {"enabled": True},
            "custom_fields": {"enabled": True},
            "remap_dependencies": {"enabled": True},
            "dependency_warning": {"enabled": True},
            "portfolios": {"enabled": True}
        },
        "name": "test_space"
    }
    space_id = client.create_space(team_id, space_payload)
    print(f"Create a space for a group of tests - {space_id}")
    # return space_id
    yield space_id
    client.delete_space(space_id)
    print(f"Delete a space for a group of tests - {space_id}\n")


@pytest.fixture(scope="class")
def folderless_list(auth_session, space):
    client = ListApiClient(auth_session)
    list_payload = {"name": "test_list"}
    list_id = client.create_folderless_list(space, list_payload)
    print(f"Create a list for a group of tests - {list_id}\n")
    # return list_id
    yield list_id
    client.delete_list(list_id)
    print(f"Delete a list for a group of tests - {list_id}")


@pytest.fixture
def default_task_payload():
    return Task(
        name="test_task"
    )


@pytest.fixture
def updated_task_payload():
    return Task(
        name="updated_test_task"
    )


@pytest.fixture(params=[
# 1. Отсутствует обязательно поле "name"
     {"description": "task without name"},
# # 2. Поле "name" слишком длинное
     {"name": "w"*10000, "description": "too long name"},
# 3. Неверный тип поля "assignees" (ожидается: array of integers)
    {"name": "task without assignees", "assignees": 42},
# 4. Неверный тип поля "description" (ожидается: string)
    {"name": "task without description", "description": True},
# # 5. Пустой json
     {},
# # 6. Несуществующее поле
     {"name": "task with fake field", "fake_field": "fake_field"},
])
def invalid_task_payload(request):
    return request.param


fake = Faker()
@pytest.fixture
def non_existent_task_id():
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choices(chars, k=10))
