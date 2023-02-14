#!/usr/bin/python3


class Rectangle:
    """This is an class Rectangle with instance attribute heigth and width"""

    def __init__(self, width, height):
        """
        initializes height and width of the rectangle
        upon creation of an instance using property
        getters and setters
        >>> my_rectangle = Rectangle(2, '4')
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer
        >>> my_rectangle = Rectangle(0, 0)
        >>> my_rectangle.width = 10
        >>> my_rectangle.height = -3
        Traceback (most recent call last):
            ...
        ValueError: height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Property setter for the width
        checks if the type for the width is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Property setter for the height
        checks if the type for the height is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

