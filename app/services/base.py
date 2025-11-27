from redis.asyncio import Redis


class Manager:
    _redis: Redis

    @property
    def redis(self) -> Redis:
        if self._redis is None:
            raise RuntimeError('Redis client has not been set.')
        return self._redis

    @classmethod
    def set_redis(cls, redis: Redis) -> None:
        cls._redis = redis
