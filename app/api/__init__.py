from typing import Any, Callable, Coroutine

from fastapi import APIRouter, Request, Response
from fastapi.routing import APIRoute
from pydantic import BaseModel

from app.utils.response import wr_o_resp


class BaseRouter(APIRouter):
    def add_api_route(
        self,
        path: str,
        endpoint: Any,
        *,
        response_model: BaseModel | None = None,
        responses: dict[int | str, dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> None:
        default = wr_o_resp(response_model)
        if responses:
            default.update(responses)
        responses = default
        return super().add_api_route(path, endpoint, response_model=response_model, responses=responses, **kwargs)


class DashRouter(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        return super().get_route_handler()

class PublicRouter(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        return super().get_route_handler()
