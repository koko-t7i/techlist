from niquests.async_api import request
from niquests.exceptions import Timeout, HTTPError
from niquests._typing import HeadersType, QueryParameterType, BodyType, AsyncBodyType, TimeoutType

from dataclasses import dataclass

from typing import Literal
from logx import log

MethodType = Literal['HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE']


@dataclass
class RetryConfig:
    max_retries: int = 5
    backoff_factor: float = 0.6
    backoff_max: float = 60
    allowed_methods: list[MethodType] = ['HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE']
    allowed_status_code: list = [408, 429, 500, 502, 503, 504]

    retry_on_status: bool = True
    retry_on_no_response: bool = False


class HttpClient:
    def __init__(self, retry_conf: RetryConfig) -> None:
        self.retry_conf = retry_conf

    async def client(
        self,
        method: MethodType,
        url: str,
        headers: HeadersType,
        params: QueryParameterType,
        data: BodyType | AsyncBodyType,
        json: dict,
        timeout: TimeoutType,
    ):
        msg = f'{method} {url} | headers: {headers} json: {json} data: {data}'
        log.info(f'req - {msg}')
        try:
            resp = await request(method=method, url=url, headers=headers, params=params, data=data, json=json, timeout=timeout)
            resp.raise_for_status()
        except HTTPError as e:
            log.error(f'E: {msg} | {e!r}')

        except Timeout as e:
            log.error(f'E: {msg} | {e!r}')

        except Exception as e:
            log.error(f'E: {e!r}')
            raise e
