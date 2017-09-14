from ..Action import Action
from ..ActionEnum import ActionEnum
from .Animal import Animal
import random

class Turtle(Animal):

    def __init__(self, animal=None, position=None, world=None):
        super(Turtle, self).__init__(animal, position, world)
        if animal is not None:
            self.moveProbability = animal.moveProbability
        else:
            self.moveProbability = 25

    def clone(self):
        return Turtle(self, None, None)

    def initParam(self):
        self.power = 2
        self.initiative = 1

    def ifAction(self):
        return random.uniform(0, 100) <= self.moveProbability

    def move(self):
        result = []
        if self.ifAction():
            positionProposals = self.world.getListOfNeighboringPositions(self.position, 2)
            if positionProposals:
                newPosition = random.choice(positionProposals)
                result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
        return result

    def diplomacy(self, atackingOrganism):
        result = []
        if atackingOrganism.power < 5:
            result.append(Action(ActionEnum.A_MOVE, atackingOrganism.lastPosition, 0, atackingOrganism))
        return result

