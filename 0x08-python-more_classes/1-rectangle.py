#!/usr/bin/python3
""" This class Defines a rectangle """


class Rectangle:
    """ Represents a rectangle.
        Args:
            width(int): The width of a rectangle
            height(int): The height of a rectangle
    """
    def __init__(self, width, height):
        """ Initializes a rectangle with those attributes """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter to give value to width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter to return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter to give value to height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
