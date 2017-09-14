from .Plant import Plant
from ..Action import Action
from ..ActionEnum import ActionEnum
from ..Position import Position

class DeadlyNightshade(Plant):
    def __init__(self, plant=None, position=None, world=None):
        super(DeadlyNightshade, self).__init__(plant, position, world)

    def clone(self):
        return DeadlyNightshade(self, None, None)

    def initParam(self):
        self.power = 99
        self.initiative = 0
        self.reproductionProbability = 30

    def consequences(self, atackingOrganism):
        result = []
        if self.power > atackingOrganism.power:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, atackingOrganism))
        else:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, self))
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, atackingOrganism))
        return result
