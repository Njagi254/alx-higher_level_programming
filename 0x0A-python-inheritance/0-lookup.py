#!/usr/bin/python3


def lookup(obj):
    """
    This function returns a list of available attributes and methods of an object.

    Parameters:
    obj (object): An object whose attributes and methods are to be returned.

    Returns:
    list: A list of available attributes and methods of the object.
    """
    return dir(obj)
