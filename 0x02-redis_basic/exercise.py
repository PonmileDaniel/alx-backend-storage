#!/usr/bin/env python3
"""
This module provides a Cache class that interacts with a Redis db.
"""
import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Storage the input data in redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
