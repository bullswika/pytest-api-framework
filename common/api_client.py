# Jiacheng
# @Time: 2025/12/10
# @Email: bullswika@outlook.com
# @File: api_client

import requests
from common.config import *
class APIClient:
    def __init__(self, base_url: str = BASE_URL, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.token = token

    def _build_headers(self, extra_headers:dict | None = None) -> dict:
        headers = {
            "Content-Type": "application/json",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if extra_headers:
            headers.update(extra_headers)
        return headers
    def get(self, path: str, params: dict | None = None, headers: dict | None = None, **kwargs):
        url = self.base_url + path
        resp = self.session.get(
            url,
            params=params,
            headers = self._build_headers(headers),
            timeout = DEFAULT_TIMEOUT,
            **kwargs
        )
        return resp

    def post(self, path: str, json:dict | None = None, headers:dict|None = None, **kwargs):
        url = self.base_url + path
        resp = self.session.post(
            url,
            json=json,
            headers = self._build_headers(headers),
            timeout = DEFAULT_TIMEOUT,
            **kwargs
        )
        return resp