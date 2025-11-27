from fastapi import Depends

from app.api import BaseRouter, DashRouter
from app.services.auth import security

from . import account

router = BaseRouter(route_class=DashRouter, dependencies=[Depends(security.access_token_required)])
router.include_router(account.router, prefix='/account', tags=['account'])
