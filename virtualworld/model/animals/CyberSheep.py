from .Sheep import Sheep
from ..Position import Position
from ..Action import Action
from ..ActionEnum import ActionEnum
import model.plants


class CyberSheep(Sheep):

    def __init__(self, animal=None, position=None, world=None):
        super(CyberSheep, self).__init__(animal, position, world)

    def clone(self):
        return CyberSheep(self, None, None)

    def initParam(self):
        self.power = 11
        self.initiative = 4

    def move(self):
        result = []
        sb = self.world.getNearestSosnowskiHogweed(self)
        if sb is not None:
            pomPos = None
            posList = self.world.getListOfNeighboringPositions(self.position, 1)
            if posList:
                pomPosDist = 1000
                for pl in posList:
                    pomDist = pl.distance(sb.position)
                    if pomDist < pomPosDist:
                        pomPos = pl
                        pomPosDist = pomDist
            if pomPos:
                result.append(Action(ActionEnum.A_MOVE, pomPos, 0, self))
        else:
            result.extend(super(CyberSheep, self).move())
        return result

    def collision(self, collisionOrganism):
        result = []
        if isinstance(collisionOrganism, model.plants.SosnowskiHogweed.SosnowskiHogweed):
            result.append(Action(ActionEnum.A_REMOVE, Position(xpos=-1, ypos=-1), 0, collisionOrganism))
        else:
            result.extend(super(CyberSheep, self).collision(collisionOrganism))
        return result

