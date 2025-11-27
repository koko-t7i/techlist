from app.api import BaseRouter
from app.api.v2 import example

v2_router = BaseRouter()

v2_router.include_router(example.router, prefix='/example')
