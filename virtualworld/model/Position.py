import math

class Position(object):
    def __init__(self, position=None, xpos=None, ypos=None):
        self.__x = 0
        self.__y = 0
        if position is not None:
            self.__x = position.x
            self.__y = position.y
        else: 
            if xpos is not None:
                self.__x = xpos
            if ypos is not None:
                self.__y = ypos

    # getters & setters

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def distance(self, position):
        if position:
            return math.sqrt((self.x - position.x) * (self.x - position.x) + (self.y - position.y) * (self.y - position.y))
        return -1

    def __eq__(self, other): 
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
