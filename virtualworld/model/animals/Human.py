import random

from .Animal import Animal
from ..Action import Action
from ..ActionEnum import ActionEnum
from ..DirectionEnum import DirectionEnum
from ..Position import Position


class Human(Animal):

    objectCounter = 0

    def __init__(self, animal=None, position=None, world=None):
        super(Human, self).__init__(animal, position, world)
        self.__counterTurnOfSkill = 0
        self.__isASkill = False
        self.__direction = DirectionEnum.STOP
        self.__runSkill = False
        Human.objectCounter += 1
        self.__objectNumber = Human.objectCounter
        if animal is not None:
            self.__objectNumber = animal.objectNumber
            self.__counterTurnOfSkill = animal.counterTurnOfSkill
            self.__isASkill = animal.isASkill
            self.__direction = animal.direction
            self.__runSkill = animal.runSkill


    def clone(self):
        return Human(self, None, None)

    def initParam(self):
        self.power = 5
        self.initiative = 4
        self.direction = DirectionEnum.STOP

    def isInteractive(self):
        return True

    @property
    def objectNumber(self):
        return self.__objectNumber

    @objectNumber.setter
    def objectNumber(self, value):
        self.__objectNumber = value

    @property
    def counterTurnOfSkill(self):
        return self.__counterTurnOfSkill

    @counterTurnOfSkill.setter
    def counterTurnOfSkill(self, value):
        self.__counterTurnOfSkill = value

    @property
    def isASkill(self):
        return self.__isASkill

    @isASkill.setter
    def isASkill(self, value):
        self.__isASkill = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def runSkill(self):
        return self.__runSkill

    @runSkill.setter
    def runSkill(self, value):
        self.__runSkill = value

    def getObjectCountrer(self):
        return Human.objectCounter

    def setObjectCountrer(self, value):
        Human.objectCountrer = value

    def positionInArrayList(self, position, positionProposals):
        pom = [p for p in positionProposals if p == position]
        if pom:
            return pom[0]
        else:
            return None


    def move(self):
        result = []
        newPosition = None
        moveDistance = 1

        if self.counterTurnOfSkill == 0:
            if self.runSkill:
                self.runSkill = False
                self.isASkill = True
                self.counterTurnOfSkill += 1
        elif self.counterTurnOfSkill < 5:
            if self.isASkill:
                self.counterTurnOfSkill += 1
            else:
                self.counterTurnOfSkill -= 1
        else: # == 5
            self.isASkill = False
            self.counterTurnOfSkill -= 1

        if self.isASkill:
            if self.counterTurnOfSkill <= 3:
                moveDistance = 2
            else:
                moveDistance = random.uniform(0, 1) + 1

        if moveDistance == 2: # move distance 2
            positionProposals = self.world.getListOfNeighboringPositions(self.position, 2)
            #
            if self.direction == DirectionEnum.FOUR_DIR_UP or self.direction == DirectionEnum.SIX_DIR_UP:
                newPosition = Position(xpos=self.position.x, ypos=self.position.y - 2)
            #
            elif self.direction == DirectionEnum.FOUR_DIR_RIGHT or self.direction == DirectionEnum.SIX_DIR_UP_RIGHT:
                if self.world.compasRose == 8: # kwadrat
                    newPosition = Position(xpos=self.position.x + 2, ypos=self.position.y)
                if self.world.compasRose == 6: # hex
                    newPosition = Position(xpos=self.position.x + 2, ypos=self.position.y - 1)
            #
            elif self.direction == DirectionEnum.SIX_DIR_DOWN_RIGHT: # prawo dol oraz prawo
                if self.world.compasRose == 6: # hex
                    newPosition = Position(xpos=self.position.x + 2, ypos=self.position.y + 1)
            #
            elif self.direction == DirectionEnum.FOUR_DIR_DOWN or self.direction == DirectionEnum.SIX_DIR_DOWN:
                newPosition = Position(xpos=self.position.x, ypos=self.position.y + 2)
            #
            elif self.direction == DirectionEnum.FOUR_DIR_LEFT or self.direction == DirectionEnum.SIX_DIR_DOWN_LEFT:
            # lewo dol oraz lewo
                if self.world.compasRose == 8: # kwadrat
                    newPosition = Position(xpos=self.position.x - 2, ypos=self.position.y)
                if self.world.compasRose == 6: # hex
                    newPosition = Position(xpos=self.position.x - 2, ypos=self.position.y + 1)
            #
            elif self.direction == DirectionEnum.SIX_DIR_UP_LEFT: #lewo gora lub lewo
                if self.world.compasRose == 6:  # hex
                    newPosition = Position(xpos=self.position.x - 2, ypos=self.position.y - 1)
            #
            else:
                return result
            if newPosition in positionProposals:
                result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
        else: # move distance = 1
            positionProposals = self.world.getListOfNeighboringPositions(self.position, 1);
            #
            if self.direction == DirectionEnum.FOUR_DIR_UP or self.direction == DirectionEnum.SIX_DIR_UP:
                newPosition = Position(xpos=self.position.x, ypos=self.position.y - 1)
            #
            elif self.direction == DirectionEnum.FOUR_DIR_RIGHT or self.direction == DirectionEnum.SIX_DIR_UP_RIGHT:
                # prawo gora lub prawo
                if self.world.compasRose == 8: # kwadrat
                        newPosition = Position(xpos=self.position.x + 1, ypos=self.position.y)
                if self.world.compasRose == 6: # hex
                    if self.position.x % 2 == 0:    # dolny w lancuchu hex
                        newPosition = Position(xpos=self.position.x + 1, ypos=self.position.y)
                    else: # gorny w lancuchu hex
                        newPosition = Position(xpos=self.position.x + 1, ypos=self.position.y - 1)
            #
            elif self.direction == DirectionEnum.SIX_DIR_DOWN_RIGHT:  # prawo dol oraz prawo
                if self.world.compasRose == 6:  # hex
                    if self.position.x % 2 == 0:   #dolny w lancuchu hex
                        newPosition = Position(xpos=self.position.x + 1, ypos=self.position.y + 1)
                    else:  # gorny w lancuchu hex
                        newPosition = Position(xpos=self.position.x + 1, ypos=self.position.y)
            #
            elif self.direction == DirectionEnum.FOUR_DIR_DOWN or self.direction == DirectionEnum.SIX_DIR_DOWN:
                newPosition = Position(xpos=self.position.x, ypos=self.position.y + 1)
            #
            elif self.direction == DirectionEnum.FOUR_DIR_LEFT or self.direction == DirectionEnum.SIX_DIR_DOWN_LEFT:
                # lewo dol oraz lewo
                if self.world.compasRose == 8:  # kwadrat
                    newPosition = Position(xpos=self.position.x - 1, ypos=self.position.y)
                if self.world.compasRose == 6:  # hex
                    if self.position.x % 2 == 0:   #dolny w lancuchu hex
                        newPosition = Position(xpos=self.position.x - 1, ypos=self.position.y + 1)
                    else:  # gorny w lancuchu hex
                        newPosition = Position(xpos=self.position.x - 1, ypos=self.position.y)
            #
            elif self.direction == DirectionEnum.SIX_DIR_UP_LEFT:  # lewo gora lub lewo
                if self.world.compasRose == 6:  # hex
                    if self.position.x % 2 == 0:  #dolny w lancuchu hex
                        newPosition = Position(xpos=self.position.x - 1, ypos=self.position.y)
                    else:   # gorny w lancuchu hex
                        newPosition = Position(xpos=self.position.x - 1, ypos=self.position.y - 1)
            else:
                return result
            #
            if newPosition in positionProposals:   # jak to sie zmienialo
                result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
        return result


    def __str__(self):
        return "{0} skillTurnCnt: {1} skillIsOn: {2}".format(super(Human, self).__str__(),
                                                             self.counterTurnOfSkill,
                                                             self.isASkill)
