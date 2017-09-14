import random

from .Animal import Animal
from ..Action import Action
from ..ActionEnum import ActionEnum


class Fox(Animal):
    def __init__(self, animal=None, position=None, world=None):
        super(Fox, self).__init__(animal, position, world)

    def clone(self):
        return Fox(self, None, None)

    def initParam(self):
        self.power = 3
        self.initiative = 7

    def move(self):
        result = []
        tmpOrganism = None
        positionProposals = self.world.getListOfNeighboringPositions(self.position, 1)
        if positionProposals:
            random.shuffle(positionProposals)
            for newPos in positionProposals:
                tmpOrganism = self.world.getOrganismFromPosition(newPos)
                if (tmpOrganism is None) or (tmpOrganism.power <= self.power):
                    result.append(Action(ActionEnum.A_MOVE, newPos, 0, self))
                    break
        return result

