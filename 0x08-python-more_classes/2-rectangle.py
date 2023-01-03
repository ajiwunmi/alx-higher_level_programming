#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize an instance of the class
        Args :
            width(int) - width of the object
            height(int) - height of the object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Calculate the area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculate the permiter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
