#!/usr/bin/python3

class Rectangle:
    """ rectange with some methods and attributes """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, x):
        try:
            if type(x) not in [int]:
                raise TypeError
            elif x < 0:
                raise ValueError
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
        self.__width = x

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, x):
        try:
            if type(x) not in [int]:
                raise TypeError
            elif x < 0:
                raise ValueError
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")
        self.__height = x
