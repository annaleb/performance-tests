from clients.http.client import HTTPClient
from httpx import Response, Client
from typing import TypedDict


class CreateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


"""
    Структура данных для создания нового пользователя.
    """


class UsersGatewayHTTPClient(HTTPClient):  # наследуем его от HTTP созданного общего клиента
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.
        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """

        :param self: Создание нового пользователя.
        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/users", json=request)

# user_client = UsersGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
# user_client.get_user_api()
# user_client.create_user_api()
