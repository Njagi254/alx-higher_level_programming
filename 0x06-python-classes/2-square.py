#!/usr/bin/python3


class Square:
    """A class that defines a square.

    Attributes:
        __size (int): Private instance attribute.
    """
    def __init__(self, size=0):
        """Initialize a square with an optional size.

        Args:
            size (int): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """int: Size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
