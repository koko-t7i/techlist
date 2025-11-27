from typing import Any

from app.api import BaseRouter
from app.api.v1 import v1_router
from app.api.v2 import v2_router

from app.utils.response import ErrorResponseModel, SuceedResponseModel, UnifiedResponse

responses: dict[int | str, dict[str, Any]] = {200: {'model': SuceedResponseModel}, 422: {'model': ErrorResponseModel}}
router = BaseRouter(default_response_class=UnifiedResponse, responses=responses)


router.include_router(v1_router, prefix='/v1', tags=['v1'])
router.include_router(v2_router, prefix='/v2', tags=['v2'])
