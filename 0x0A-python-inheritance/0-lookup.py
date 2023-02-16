#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methods of an object.

    Parameters:
    obj (object): The object whose attributes and methods will be returned.

    Returns a list of the object's available attributes and methods.
    """
    return dir(obj)
