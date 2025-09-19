from src.utils.helpers import CLICKUP_API_KEY, CLICKUP_EMAIL, CLICKUP_PASSWORD
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ApiConstants:
    BASE_URL: str = "https://api.clickup.com"
    AUTH_DATA: dict = field(default_factory=lambda:{
        "Authorization": CLICKUP_API_KEY,
        "accept": "application/json"
    })
    API_HEADERS: dict = field(default_factory=lambda:{
        "accept": "application/json",
        "content-type": "application/json"
    })


api_config = ApiConstants()
