# Jiacheng
# @Time: 2025/12/10
# @Email: bullswika@outlook.com
# @File: api_client
import allure
import requests
from common.config import *
import logging
import time
from typing import Any


logger = logging.getLogger(__name__)

def _mask_token(token: str | None) -> str | None:
    if not token:
        return token
    if len(token) <= 6:
        return "***"
    return token[:3] + "***" + token[-3:]


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

    def _log_request(self, method: str, url: str, *, params=None, json=None, headers=None):
        safe_headers = dict(headers or {})
        if "Authorization" in safe_headers:
            safe_headers["Authorization"] = f"Bearer {_mask_token(self.token)}"

        logger.info(
            "[REQ] %s %s | params=%s | json=%s | headers=%s",
            method, url, params, json, safe_headers
        )

        #  step 放这里
        with allure.step(f"{method} {url}"):
            allure.attach(
                name="Request",
                body=(
                    f"Headers:\n{safe_headers}\n\n"
                    f"Params:\n{params}\n\n"
                    f"JSON:\n{json}"
                ),
                attachment_type=allure.attachment_type.TEXT
            )

    def _log_response(self, method: str, url: str, resp, elapsed_ms: int):
        try:
            text = resp.text
        except Exception:
            text = "<no text>"

        if text and len(text) > 800:
            text = text[:800] + "...(truncated)"

        level = logging.INFO if resp.status_code < 400 else logging.ERROR
        logger.log(
            level,
            "[RESP] %s %s | %s | %dms | body=%s",
            method, url, resp.status_code, elapsed_ms, text
        )

        allure.attach(
            name="Response",
            body=(
                f"Status: {resp.status_code}\n"
                f"Time: {elapsed_ms} ms\n\n"
                f"Body:\n{text}"
            ),
            attachment_type=allure.attachment_type.TEXT
        )

    def get(self, path: str, params: dict | None = None, headers: dict | None = None, **kwargs):
        url = self.base_url + path
        built_headers = self._build_headers(headers)
        self._log_request("GET", url, params=params, json=None, headers=built_headers)
        start = time.time()
        resp = self.session.get(
            url,
            params=params,
            headers = built_headers,
            timeout = DEFAULT_TIMEOUT,
            **kwargs
        )
        elapsed_ms = int((time.time() - start) * 1000)
        self._log_response("GET", url, resp, elapsed_ms)
        return resp

    def post(self, path: str, json:dict | None = None, headers:dict|None = None, **kwargs):
        url = self.base_url + path
        built_headers = self._build_headers(headers)
        self._log_request("POST", url, params=None, json=json, headers=built_headers)
        start = time.time()
        resp = self.session.post(
            url,
            json=json,
            headers = built_headers,
            timeout = DEFAULT_TIMEOUT,
            **kwargs
        )
        elapsed_ms = int((time.time() - start) * 1000)

        self._log_response("POST", url, resp, elapsed_ms)
        return resp
    def create_user(self,payload:dict):
        return self.post("/users", json=payload)
