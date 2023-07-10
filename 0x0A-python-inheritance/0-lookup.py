#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """returns all objects in an objects dictionary
        -> as a list
    """
    return dir(obj)
