from app.api import BaseRouter
from app.api.v1 import example, dash

v1_router = BaseRouter()
v1_router.include_router(dash.router, prefix='/dash', tags=['dash'])

v1_router.include_router(example.router, prefix='/example')
