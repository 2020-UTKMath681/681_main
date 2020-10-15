'''Demonstrates the use of getters/setters
'''

from math import exp

class clip_x:

    def __init__(self, x):
        """
        This class has a property x which is auto-bounded between 0 and 1 using
        clipping. This is accomplished using a getter/setter for the property
        and a private attribute holding the necessary information internally.
        """

        # Though this looks like normal attribute assignment, it actually calls
        #   the setter method below
        self.x = x


    @property # This decorator turns this getter method into a property
    def x(self):
        # Simply return the internal version, __x
        return self.__x # two underscores are convention for "private"


    @x.setter # This decorator makes this method a getter for property x
    def x(self, x):
        # note that x inside this function refers to the argument
        if x < 0:
            self.__x = 0
        elif x > 1:
            self.__x = 1
        else:
            self.__x = x

    @property
    def e_to_x(self):
        # read-only property that returns e^x
        return exp(self.__x)
