#!/usr/bin/python3


"""
def lookup(obj):
    """
    This function returns the list of available attributes and methods of an object.
    
    Parameters:
    obj (object): The object whose attributes and methods will be returned.
    
    Returns:
    list: A list of the object's available attributes and methods.
    """
    return [attr for attr in dir(obj) if not attr.startswith('__')]
