#!/usr/bin/env python3
"""
Insert a doc 
"""


def insert_school(mongo_collection, **kwargs):
    """
    INsert a new doc
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
