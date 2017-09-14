from .Plant import Plant
from ..Action import Action
from ..ActionEnum import ActionEnum
from ..Position import Position
from ..animals.CyberSheep import CyberSheep

class SosnowskiHogweed(Plant):
    def __init__(self, plant=None, position=None, world=None):
        super(SosnowskiHogweed, self).__init__(plant, position, world)

    def clone(self):
        return SosnowskiHogweed(self, None, None)

    def initParam(self):
        self.power = 10
        self.initiative = 0
        self.reproductionProbability = 30

    def move(self):
        result = []
        newPosition = None
        newPlant = None
        if self.ifReproduce():
            result.extend(super(SosnowskiHogweed, self).move())
        neighboringPositions = self.world.getListOfNeighboringPositions(self.position, 1)
        pomOrganism = None
        for pomPosition in neighboringPositions:
            pomOrganism = self.world.getOrganismFromPosition(pomPosition)
            if pomOrganism is not None:
                 if not isinstance(pomOrganism, (Plant, CyberSheep)):
                    result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, pomOrganism))
        return result
    
    def consequences(self, atackingOrganism):
        result = []
        if self.power > atackingOrganism.power:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, atackingOrganism))
        else:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, self))
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, atackingOrganism))
        return result
