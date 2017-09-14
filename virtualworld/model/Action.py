#-*- coding: utf-8 -*-

from .ActionEnum import *
from .Position import Position

class Action(object):
    def __init__(self, action, position, value, organism):
        self.__action = action
        self.__position = position
        self.__value = value
        self.__organism = organism

    # getters & setters

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def organism(self):
        return self.__organism

    @organism.setter
    def organism(self, value):
        self.__organism = value

    def __str__(self):
        nazwaKlasy = self.organism.__class__.__name__
        wybor = {ActionEnum.A_ADD :  "{0}: dodanie na pozycję: {1}".format(nazwaKlasy, self.position),
                ActionEnum.A_INCREASEPOWER : "{0}: zwiększenie siły o: {1}".format(nazwaKlasy, self.value),
                ActionEnum.A_MOVE : "{0}: zmiana pozycji z: {1} na: {2}".format(nazwaKlasy,
                                                            self.organism.position, self.position),
                ActionEnum.A_REMOVE : "{0}: usunięcie z pozycji: {1}".format(nazwaKlasy, self.position)
        }
        return wybor[self.action]
 