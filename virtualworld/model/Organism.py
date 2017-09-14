import abc
from abc import ABC, abstractmethod, abstractproperty
from .Position import Position
from .Action import Action
from .ActionEnum import ActionEnum


class Organism(ABC):

    def __init__(self, organizm, position, world):
        self.__power = None
        self.__initiative = None
        self.__position = None
        self.__world = None
        self.__color = None
        if organizm is not None:
            self.__power = organizm.power
            self.__initiative = organizm.initiative
            self.__position = Position(organizm.position)
            self.__world = organizm.world
            self.__color = organizm.color
        else: 
            if position is not None:
                self.__position = position
            if world is not None:
                self.__world = world
    
    # getters & setters

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        self.__power = value

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, value):
        self.__initiative = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def world(self):
        return self.__world

    @world.setter
    def world(self, value):
        self.__world = value

    def isInteractive(self):
        return False

    @abstractmethod
    def initParam(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def collision(self, collisionOrganism):
        pass

    @property
    @abstractmethod
    def lastPosition(self):
        pass

    @lastPosition.setter
    @abstractmethod
    def lastPosition(self, value):
        pass

    def diplomacy(self, atackingOrganism):
        return []

    def consequences(self, atackingOrganism):
        result = []
        if self.power > atackingOrganism.power:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, atackingOrganism))
        else:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, self))
        return result


    def __str__(self):
        return "{0}: power: {1} initiative: {2} position: {3}"\
                    .format(self.__class__.__name__, self.power, self.initiative, self.position)

