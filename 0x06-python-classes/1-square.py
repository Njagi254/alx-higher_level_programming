#!/usr/bin/python3
"""This class represents a square"""


class Square:
    """Constructor for Square class"""
    def __init__(self, size):
        """Initializes Square object with given size"""
        self.__size = size  # private instance attribute

    """Getter for size attribute"""
    def get_size(self):
        return self.__size
