#!/usr/bin/env python3
"""
This module provides a Cache class that interacts with a Redis db.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count
    """

    @wraps(methd)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self.redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Cache class for storing and retrieving data
    """

    def __init__(self) -> None:
        """
        Initialize the Redis client and flush
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Storage the input data in redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None,
    ) -> Union[str, int, float, bytes, None]:
        """
        Retrieve the data stored
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 decode
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer
        """
        return sZZelf.get(key, fn=int)
