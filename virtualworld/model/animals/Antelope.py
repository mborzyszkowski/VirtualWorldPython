from ..Action import Action
from ..ActionEnum import ActionEnum
from .Animal import Animal
import random

class Antelope(Animal):
    
    def __init__(self, animal=None, position=None, world=None):
        super(Antelope, self).__init__(animal, position, world)
        self.escapeProbability = 50
    
    def clone(self):
        return Antelope(self, None, None)

    def initParam(self):
        self.power = 4
        self.initiative = 4
    
    def move(self): 
        result = []
        positionProposals = self.world.getListOfNeighboringPositions(self.position, 2)
        if positionProposals:
            newPosition = random.choice(positionProposals)
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
        return result
    
    def diplomacy(self, atackingOrganism):
        result = []
        escapePosition = None
        if self.ifRun():
            escapePosition = self.world.getFreeNeighboringPosition(self.position)
            if self.world.positionOnBoard(escapePosition):
                result.append(Action(ActionEnum.A_MOVE, escapePosition, 0, self))
        return result

    def ifRun(self):
        return random.uniform(0, 100) <= self.escapeProbability
