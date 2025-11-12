from __future__ import annotations

from httpx import Client, URL, QueryParams, Response
from typing import Any


class HTTPClient:  # создаем класс Базовый HTTP API клиент, принимающий объект httpx.Client
    def __init__(self, client: Client):  # создаем конструктор класса
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    def post(self, url: URL | str, json: Any | None = None) -> Response:
        return self.client.post(url, json=json)
