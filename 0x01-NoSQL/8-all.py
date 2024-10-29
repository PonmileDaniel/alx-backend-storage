#!/usr/bin/env python3
"""
List all doc in python
"""

def list_all(mongo_collection):
    """
    LIst all the doc in the collection
    """
    return mongo_collection.find()
