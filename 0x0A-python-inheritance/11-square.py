#!/usr/bin/python3
""" creating a class"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A square class that inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)


    def area(self):
        """ area method """
        retun self.__size ** 2

    def __str__(self):
        """__str__method"""
        return "[Square] {}/{}".format(self.__size, self.__size)

