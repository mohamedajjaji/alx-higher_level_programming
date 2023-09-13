#!/usr/bin/python3
""" Defines class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle """

    def __init__(self, size):
        """ Initialize a new square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
