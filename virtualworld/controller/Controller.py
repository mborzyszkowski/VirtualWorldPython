import math
from wx.lib.ogl.basic import RectangleShape, OP_CLICK_LEFT
from model.Position import Position
from model.DirectionEnum import DirectionEnum
from model.animals.Human import Human
from model.OrganismFactory import OrganismFactory
from view.HexagonShape import HexagonShape
from controller.WorldCell import WorldCell
import pickle

class Controller:
    def __init__(self, app, model, view):
        self.model = model
        self.view = view

        self.view.setController(self)

        #self.view.set_ogranisms_to_canvas()
        # self.view.diagram.ShowAll(1)
        # self.view.Show()


    def getTurnNumber(self):
        return self.model.turn

    def performNextTurn(self):
        self.model.makeTurn()

    def getActionLoggerReport(self):
        return  str(self.model.actionLogger)

    def addOrganism(self, species, position):
        factory = OrganismFactory()
        organism = factory.createOrganism(species, position)
        organism.world = self.model
        return self.model.addOrganism(organism)

    def getWorldMap(self):
        map = []
        pomWorldRow = []
        org = None
        shape = None
        siteLenght = self.view.getSideMapLenght()
        shift = siteLenght
        triangleheight = siteLenght * math.sqrt(3.0) / 2.0
        for y in range(0, self.model.boardY):
            for x in range(0, self.model.boardX):
                org = self.model.getOrganismFromPosition(Position(xpos=x, ypos=y))
                if self.model.compasRose == 8:
                    shape = RectangleShape(siteLenght, siteLenght)
                    shape.SetX(x * siteLenght + shift/2)
                    shape.SetY(y * siteLenght + shift/2)
                elif x % 2 == 0:
                    shape = HexagonShape(siteLenght)
                    shape.SetX(x * (siteLenght + triangleheight / 2) + siteLenght + triangleheight)
                    shape.SetY((y + 1) * 2 * triangleheight + shift)
                else:
                    shape = HexagonShape(siteLenght)
                    shape.SetX(x * (siteLenght + triangleheight / 2) + siteLenght + triangleheight)
                    shape.SetY(y * 2 * triangleheight + triangleheight + shift)
                #shape.Show(True)
                shape.SetSensitivityFilter(sens=OP_CLICK_LEFT)
                if org is not None:
                    pomWorldRow.append(WorldCell(x, y, org.color, False, shape))
                else:
                    pomWorldRow.append(WorldCell(x, y, "WHITE", True, shape))
            map.append(pomWorldRow)
            pomWorldRow = []
        return map

    def saveModel(self, fileName):
        objOut = open(fileName, 'wb')
        pickle.dump(self.model, objOut)
        objOut.close()

    def loadModel(self, fileName):
        objOut = open(fileName, 'rb')
        self.model = pickle.load(objOut)
        objOut.close()

    def canTurnHumanSkillOn(self):
        org = self.model.getHuman()
        result = False
        if org is not None:
            if type(org) == Human:
                if org.counterTurnOfSkill == 0 and not org.isASkill:
                    return True
        return False

    def turnHumanSkillOn(self):
        org = self.model.getHuman()
        if org is not None:
            if type(org) == Human:
                if org.counterTurnOfSkill == 0 and not org.isASkill:
                    org.runSkill = True

    def getHumanStatus(self):
        org = self.model.getHuman()
        result = "Human: "
        if org is not None:
            if type(org) == Human:
                if org.direction == DirectionEnum.FOUR_DIR_UP or org.direction == DirectionEnum.SIX_DIR_UP:
                    result += "up"
                elif org.direction == DirectionEnum.FOUR_DIR_DOWN or org.direction == DirectionEnum.SIX_DIR_DOWN:
                    result += "down"
                elif org.direction == DirectionEnum.FOUR_DIR_LEFT:
                    result += "left"
                elif org.direction == DirectionEnum.FOUR_DIR_RIGHT:
                    result += "right"
                elif org.direction == DirectionEnum.SIX_DIR_DOWN_LEFT:
                    result += "down left"
                elif org.direction == DirectionEnum.SIX_DIR_DOWN_RIGHT:
                    result += "down right"
                elif org.direction == DirectionEnum.SIX_DIR_UP_RIGHT:
                    result += "up right"
                elif org.direction == DirectionEnum.SIX_DIR_UP_LEFT:
                    result += "up left"
                elif org.direction == DirectionEnum.STOP:
                    result += "stop"
            else:
                result += "no Human"
        else:
            result +="no Human"
        return result

    def getHumanCounterTurnOfSkill(self):
        counter = -1
        org = self.model.getHuman()
        if org is not None:
            if type(org) == Human:
                counter = org.counterTurnOfSkill
        return counter
