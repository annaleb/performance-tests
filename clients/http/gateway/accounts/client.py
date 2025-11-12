from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict


class GetAccountsQueryDict(TypedDict):
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    userId: str


class OpenDebitCardAccountRequestDict(TypedDict):
    userId: str


class OpenCreditCardAccountRequestDict(TypedDict):
    userId: str
    # Создание образа клиента для аккаунта ендпоинта


class AccountGatewayHTTPClient(HTTPClient):
    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        return self.get("/api/v1/accounts", params=query)

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.
        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)

