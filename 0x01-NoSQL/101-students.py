#!/usr/bin/env python3
"""
Top
"""


def top_students(mongo_collection):
    """
    return all student
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
        ])
