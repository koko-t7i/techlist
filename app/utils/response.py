from typing import Any, Mapping

from fastapi import BackgroundTasks
from fastapi.responses import ORJSONResponse as JSONResponse
from pydantic import BaseModel
from starlette.background import BackgroundTask


class UnifiedResponseModel(BaseModel):
    success: bool = True
    msg: str = "ok"
    data: None | Any = None


class SuceedResponseModel(BaseModel):
    success: bool = True
    msg: str = "ok"
    data: None = None


class ErrorResponseModel(BaseModel):
    success: bool = False
    msg: str
    trace_id: str


def wr_o_resp(model: BaseModel | None) -> dict[int | str, dict[str, Any]]:
    if model:
        wrapper_name = f"{model.__name__}Response"
        Wrapped = type(wrapper_name, (UnifiedResponseModel,), {"__annotations__": {"data": model}})
    else:
        Wrapped = type("NoneResponse", (UnifiedResponseModel,), {"__annotations__": {"data": None}})
    return {200: {"model": Wrapped}}


class UnifiedResponse(JSONResponse):
    def __init__(
        self,
        data: Any,
        status_code: int = 200,
        msg: str = "ok",
        headers: dict[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTasks | None = None,
    ):
        _content = UnifiedResponseModel(success=True, msg=msg, data=data)
        super().__init__(
            _content.model_dump(),
            status_code=status_code,
            headers=headers,
            media_type=media_type,
            background=background,
        )


class ErrorResponse(JSONResponse):
    def __init__(
        self,
        trace_id: str,
        status_code: int,
        msg: str = "error",
        headers: Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,
    ) -> None:
        _content = ErrorResponseModel(success=False, msg=msg, trace_id=trace_id)
        super().__init__(
            _content.model_dump(),
            status_code=status_code,
            headers=headers,
            media_type=media_type,
            background=background,
        )
