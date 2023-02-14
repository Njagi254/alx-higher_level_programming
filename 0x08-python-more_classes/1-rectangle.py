#!/usr/bin/python3


class Rectangle:
    """
    Class for representing and manipulating rectangles
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with given width and height

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError: If either width or height is not an int
            ValueError: If either width or height is negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            The width of the rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            value (int): The width of the rectangle

        Raises:
            TypeError: If width is not an int
            ValueError: If width is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            The height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value (int): The height of the rectangle

        Raises:
            TypeError: If height is not an int
            ValueError: If height is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
