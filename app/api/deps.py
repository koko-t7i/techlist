from typing import Annotated

from fastapi import Depends, Request

from app.services.account import AccountManage
from app.services.auth import AuthManage
from app.services.example import ExampleManage


def get_example_mgt() -> ExampleManage:
    return ExampleManage()


def get_account_mgt(request: Request) -> AccountManage:
    return AccountManage()


def get_auth_mgt(request: Request) -> AuthManage:
    return AuthManage()

ExampleMgt = Annotated[ExampleManage, Depends(get_example_mgt)]
AccountMgt = Annotated[AccountManage, Depends(get_account_mgt)]
