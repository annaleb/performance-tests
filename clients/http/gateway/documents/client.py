from clients.http.client import HTTPClient
from httpx import Response


class TariffDocumentsGatewayHTTPClient(HTTPClient):
    def get_tariff_documents_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")


class ContractDocumentsGatewayHTTPClient(HTTPClient):
    def get_contract_documents_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")
