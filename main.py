from typing import AsyncGenerator

import nanoid
import sentry_sdk
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.routing import APIRoute
from redis.asyncio import Redis
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import RegisterTortoise

from app.api.router import router
from app.services.base import Manager
from config import CONF


def custom_generate_unique_id(route: APIRoute) -> str:
    _id = nanoid.generate()
    return f'{route.tags[0]}-{route.name}-{_id}'


if CONF.SENTRY_DSN and CONF.ENVIRONMENT != 'local':
    sentry_sdk.init(dsn=str(CONF.SENTRY_DSN), enable_tracing=True)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # * Redis
    redis = Redis.from_url(url=CONF.REDIS_URL, decode_responses=True, retry_on_timeout=False)
    app.state.redis = redis
    Manager.set_redis(app.state.redis)

    # * Tortoise ORM
    async with RegisterTortoise(app, db_url=CONF.ORM_URL, modules=CONF.APP_MODELS, generate_schemas=True):
        yield

    await redis.close()


app = FastAPI(
    title=CONF.PROJECT_NAME,
    openapi_url=f'{CONF.API_V1_STR}/openapi.json',
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan,
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)
