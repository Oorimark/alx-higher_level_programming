#!/usr/bin/python3

class Rectangle:
    """ rectange with some methods and attributes """
    def __init__(self, width=0, height=0):
        """ initiate the width and height of the rectangle

            Attributes:
                self.height: setter for the height property
                self.width: setter fo the width property
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, x):
        """ Set the width of the rectangle """
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
        """ height property """
        return self.__height

    @height.setter
    def height(self, x):
        """ Set the height of the rectangle """
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
