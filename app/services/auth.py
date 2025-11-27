from authx import AuthX, AuthXConfig
from app.services.base import Manager
from config import CONF


class AuthManage(Manager):
    config = AuthXConfig(
        JWT_ALGORITHM='HS256',
        JWT_SECRET_KEY=CONF.SECRET_KEY,
        JWT_TOKEN_LOCATION=['headers'],
    )

    def __init__(self) -> None:
        super().__init__()
        self.auth = AuthX(config=self.config)

    

auth_mgt = AuthManage()
security = auth_mgt.auth
