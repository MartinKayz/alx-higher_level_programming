#!/usr/bin/python3
""" This class Defines a rectangle """


class Rectangle:
    """ Represents a rectangle.
        Args:
            width(int): The width of a rectangle
            height(int): The height of a rectangle
    """
    def __init__(self, width=0, height=0):
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

    def area(self):
        """ Returns the area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of a rectangle"""
        if self.__height == 0 or self.width == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """ Returns a nicely formatted Representation of rectangle as # """
        if self.__height == 0 or self.__width == 0:
            return ''
        rows = []
        for i in range(self.__height):
            row = '#' * self.__width
            rows.append(row)
        return "\n".join(rows)

    def __repr__(self):
        """ Returns the caconical repressentation
            of the rectangle object as #'s """
        return f"Rectangle({self.__width}, {self.__height})"
