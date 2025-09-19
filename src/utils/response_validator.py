import pytest
from attr.filters import exclude
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type


def validate_response(
    response: Response,
    model: Type[BaseModel],
    expected_status: int = 200,
    expected_data: dict | None = None,
    exclude_fields: set | None = None
) -> BaseModel:
    """
    Универсальный валидатор ответа API:
    - Проверка status_code
    - Валидация схемы через Pydantic
    - Сравнение с ожидаемыми данными (опционально)

    :return: объект модели
    """

    # проверка кода ответа
    if response.status_code != expected_status:
        pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")

    # парсинг JSON
    try:
        data = response.json()
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")

    # Валидация схемы Pydantic
    try:
        parsed = model(**data)
    except ValidationError as e:
        pytest.fail(f"Pydantic валидация не прошла:\n{e}")

    # Сравнение с ожидаемыми данными(проверка только переданных полей)
    if expected_data:
        # Обернём данные в такую же модель для сравнения
        expected_model = model(**expected_data)
        actual_data = parsed.model_dump(exclude=exclude_fields or set())
        expected_data = parsed.model_dump(exclude=exclude_fields or set())

        if actual_data != expected_data:
            pytest.fail(
                f"Данные ответа не совпадают с ожидаемыми:\n"
                f"Expected: {expected_data}\n"
                f"Actual:   {actual_data}"
            )

    return parsed
