import random
from ..Action import Action
from ..ActionEnum import ActionEnum
from ..Organism import Organism
# from ..Position import Position
from abc import abstractmethod

class Plant(Organism):
    def __init__(self, plant=None, position=None, world=None):
        super(Plant, self).__init__(plant, position, world)
        if plant:
            self.__reproductionProbability = plant.reproductionProbability
        else:
            self.__reproductionProbability = 30

    @abstractmethod
    def clone(self):
        pass

    @property
    def reproductionProbability(self):
        return self.__reproductionProbability

    @reproductionProbability.setter
    def reproductionProbability(self, value):
        self.__reproductionProbability = value

    def ifReproduce(self):
        return random.uniform(0, 100) <= self.reproductionProbability

    def move(self):
        result = []
        newPosition = None
        newPlant = None
        if self.ifReproduce():
            newPosition = self.world.getFreeNeighboringPosition(self.position)
            if self.world.positionOnBoard(newPosition):
                newPlant = self.clone()
                newPlant.initParam()
                newPlant.position = newPosition
                result.append(Action(ActionEnum.A_ADD, newPosition, 0, newPlant))
        return result

    def collision(self, CollisionOrganism):
        result = []
        return result

    @property
    def lastPosition(self):
        return self.position

    @lastPosition.setter
    def lastPosition(self, value):
        self.position = value

    def setPosition(self, pos, back):
        self.position = pos

