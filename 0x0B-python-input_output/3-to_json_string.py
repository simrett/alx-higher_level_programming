#!/usr/bin/python3
"""Defines a string-to-JSON function."""

import json


def to_json_string(my_obj):
    """returs json string containing object's representation."""
    return json.dumps(my_obj)