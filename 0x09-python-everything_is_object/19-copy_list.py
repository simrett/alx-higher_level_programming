#!/usr/bin/python3


def copy_list(l):
    """generate a copy of a list
    """
    if not isinstance(l, list):
        return None
    return l[:]
