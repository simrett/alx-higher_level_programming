#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """reads a file
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
