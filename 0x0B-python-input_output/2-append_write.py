#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """appends onto a encoded text file
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
