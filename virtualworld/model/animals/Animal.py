import random
from ..Action import Action
from ..ActionEnum import ActionEnum
from ..Organism import Organism
from ..Position import Position
from abc import abstractmethod


class Animal(Organism):

    def __init__(self, animal=None, position=None, world=None):
        super(Animal, self).__init__(animal, position, world)
        if position is not None:
            self.__lastPosition = Position(position)
        elif animal is not None:
            self.__lastPosition = Position(animal.position)

    @abstractmethod
    def clone(self):
        pass

    def move(self): 
        result = []
        positionProposals = self.world.getListOfNeighboringPositions(self.position, 1)
        if positionProposals:
            newPosition = random.choice(positionProposals)
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
        return result

    def collision(self, collisionOrganism):
        result = []
        pomArray = []
        newPosition = None
        newAnimal = None
        if collisionOrganism is not None:
            if type(self) == type(collisionOrganism):
                result.append(Action(ActionEnum.A_MOVE, self.lastPosition, 0, self))
                newPosition = self.world.getFreeNeighboringPosition(self.position,exclude=self.lastPosition)
                if (not newPosition.x == -1) and (not newPosition.y == -1) and \
                    (not newPosition.x == self.lastPosition.x) and (not newPosition.y == self.lastPosition.y): 
                    newAnimal = self.clone()
                    newAnimal.initParam()
                    newAnimal.position = newPosition
                    result.append(Action(ActionEnum.A_ADD, newPosition, 0, newAnimal))
            else:
                pomArray = collisionOrganism.diplomacy(self)
                if not pomArray:
                    result = collisionOrganism.consequences(self)
                else:
                    result = pomArray
        return result

    def setPosition(self, pos, back):
        if back:
            self.lastPosition = self.position
        self.position = pos

    @property
    def lastPosition(self):
        return self.__lastPosition

    @lastPosition.setter
    def lastPosition(self, value):
        self.__lastPosition = value

    def __str__(self):
        return "{0}: lastPosition: {1}".format(super(Animal, self).__str__(), self.lastPosition)
