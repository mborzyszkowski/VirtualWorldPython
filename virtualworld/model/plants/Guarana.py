from .Plant import Plant
from ..Action import Action
from ..ActionEnum import ActionEnum
from ..Position import Position

class Guarana(Plant):
    def __init__(self, plant=None, position=None, world=None):
        super(Guarana, self).__init__(plant, position, world)

    def clone(self):
        return Guarana(self, None, None)

    def initParam(self):
        self.power = 0
        self.initiative = 0
        self.reproductionProbability = 30

    def consequences(self, atackingOrganism):
        result = []
        if self.power > atackingOrganism.power:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, atackingOrganism))
        else:
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, self))
            result.append(Action(ActionEnum.A_INCREASEPOWER, Position(xpos=-1, ypos=-1), 3, atackingOrganism))
        return result

