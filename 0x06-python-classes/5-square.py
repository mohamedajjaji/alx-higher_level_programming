#!/usr/bin/python3
""" Class """


class Square:
    """ Class Square """

    def __init__(self, size=0):
        """ onstructor of a Square with size """
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """ Method to get the area of a Square """
        return (self.__size ** 2)

    def my_print(self):
        """ Method to print a Square """
        if (self.__size == 0):
            print()
        else:
            for rows in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """ Getter of the private attribute size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter for the size private attribute """
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
