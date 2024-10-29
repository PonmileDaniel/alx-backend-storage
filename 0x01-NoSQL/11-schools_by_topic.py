#!/usr/bin/env python3
"""
School topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return list of school with specific topis
    """
    return mongo_collection.find({"topics": topic})
