from .ActionLogger import ActionLogger
from .ActionEnum import *
from .Position import Position
from .animals.Human import Human
from .plants.SosnowskiHogweed import SosnowskiHogweed
import random

class World(object):

    def __init__(self, boardX, boardY, compasRose):
        self.__organisms=[]
        self.__newOrganisms = []
        self.__actionLogger = ActionLogger()
        self.__boardX = boardX
        self.__boardY = boardY
        self.__turn = 0
        self.__compasRose = compasRose

    @property
    def boardX(self):
        return self.__boardX

    @boardX.setter
    def boardX(self, value):
        self.__boardX = value

    @property
    def boardY(self):
        return self.__boardY

    @boardY.setter
    def boardY(self, value):
        self.__boardY = value

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value

    @property
    def compasRose(self):
        return self.__compasRose

    @compasRose.setter
    def compasRose(self, value):
        self.__compasRose = value

    @property
    def organisms(self):
        return self.__organisms

    @organisms.setter
    def organisms(self, value):
        self.__organisms = value

    @property
    def newOrganisms(self):
        return self.__newOrganisms

    @newOrganisms.setter
    def newOrganisms(self, value):
        self.__newOrganisms = value

    @property
    def actionLogger(self):
        return self.__actionLogger

    def makeMove(self, action):
        if action.action == ActionEnum.A_MOVE:
            self.actionLogger.addDescriptions("{0}: zmiana pozycji z: {1} na: {2}"\
                        .format(action.organism.__class__.__name__,
                                action.organism.position,
                                action.position))
            action.organism.setPosition(action.position, True)
        elif action.action == ActionEnum.A_REMOVE:
            self.actionLogger.addDescriptions("{0}: usunięcie z pozycji: {1}" \
                        .format(action.organism.__class__.__name__,
                                action.organism.position))
            action.organism.setPosition(Position(xpos=-1, ypos=-1), True)
        elif action.action == ActionEnum.A_ADD:
            self.actionLogger.addDescriptions("{0}: dodanie na pozycję: {1}"\
                        .format(action.organism.__class__.__name__,
                                action.position))
            self.newOrganisms.append(action.organism)
        elif action.action == ActionEnum.A_INCREASEPOWER:
            self.actionLogger.addDescriptions("{0}: zwiększenie siły o: {1}"\
                    .format(action.organism.__class__.__name__,
                            action.value))
            action.organism.power += action.value

    def makeTurn(self):
        actions = []
        self.actionLogger.clear()
        for o in self.organisms:
            # Move
            pomPosition = o.position
            if (pomPosition.x >= 0) and (pomPosition.y >= 0):
                actions = o.move()
                for a in actions:
                    self.makeMove(a)
                actions = []
                pomPosition = o.position
                o.setPosition(Position(xpos=-1, ypos=-1), False)
                collisionOrganism = self.getOrganismFromPosition(pomPosition)
                o.setPosition(pomPosition, False)
                # Collision
                actions = o.collision(collisionOrganism)
                for a in actions:
                    self.makeMove(a)
            actions = []
        # remove each Organism with position (-1, -1)
        self.organisms = [org for org in self.organisms if not (org.position.x == -1) and not (org.position.y == -1)]
        self.newOrganisms = [org for org in self.newOrganisms if not (org.position.x == -1) and not (org.position.y == -1)]
        # add newOrganisms to Organisms
        self.organisms.extend(self.newOrganisms)
        self.organisms.sort(key=lambda org: org.initiative, reverse=True)
        self.newOrganisms = []
        self.turn += 1

    def addOrganism(self, newOrganism):
        pomX = newOrganism.position.x
        pomY = newOrganism.position.y
        if (pomX >= 0) and (pomY >= 0) and (pomX < self.boardX) and (pomY < self.boardY):
            self.organisms.append(newOrganism)
            self.organisms.sort(key=lambda org: org.initiative, reverse=True)
            return True
        else:
            return False

    def getOrganismFromPosition(self, position):
        pomOrganism = None
        for o in self.organisms:
            if o.position == position:
                pomOrganism = o
                break
        for o in self.newOrganisms:
            if o.position == position:
                pomOrganism = o
                break
        return pomOrganism


    def getFreePositionInWorld(self):
        freePosition = []
        for y in range(0, self.boardY):
            for x in range(0, self.boardX):
                p = Position(xpos=x, ypos=y)
                if self.getOrganismFromPosition(p) is None:
                    freePosition.append(p);
        if not freePosition:
            return Position(xpos=-1, ypos=-1)
        return random.choice(freePosition)

    def positionOnBoard(self, position):
        return position.x >= 0 and position.y >= 0 and position.x < self.boardX and position.y < self.boardY

    def getFreeNeighboringPosition(self, position, exclude=None):
        pomNeighboringPositions = self.getListOfNeighboringPositions(position, 1)
        for pos in pomNeighboringPositions:
            if exclude is not None:
                if pos == exclude:
                    continue
            if self.getOrganismFromPosition(pos) is None:
                return pos
        return Position(xpos=-1, ypos=-1)


    def getListOfNeighboringPositions(self, position, distance):
        result = []
        shifts = []
        if self.compasRose == 8:
            if distance == 1:
                shiftsArray = [
                    Position(xpos=-1, ypos=-1), Position(xpos=0, ypos=-1), Position(xpos=1, ypos=-1),
                    Position(xpos=1, ypos=0), Position(xpos=1, ypos=1), Position(xpos=0, ypos=1),
                    Position(xpos=-1, ypos=1), Position(xpos=-1, ypos=0)
                ]
                shifts.extend(shiftsArray)
            elif distance == 2:
                shiftsArray = [
                    Position(xpos=-2, ypos=-2), Position(xpos=-1, ypos=-2), Position(xpos=0, ypos=-2), Position(xpos=1, ypos=-2),
                    Position(xpos=2, ypos=-2), Position(xpos=2, ypos=-1), Position(xpos=2, ypos=0), Position(xpos=2, ypos=1),
                    Position(xpos=2, ypos=2), Position(xpos=1, ypos=2), Position(xpos=0, ypos=2), Position(xpos=-1, ypos=2),
                    Position(xpos=-2, ypos=2), Position(xpos=-2, ypos=1), Position(xpos=-2, ypos=0), Position(xpos=-2, ypos=-1)
                ]
                shifts.extend(shiftsArray)
        elif self.compasRose == 6:
            if distance == 1:
                if position.x % 2 == 0:
                    # dolny w lancuchu
                    shiftsArray = [
                        Position(xpos=0, ypos=-1), Position(xpos=1, ypos=0), Position(xpos=1, ypos=1),
                        Position(xpos=0, ypos=1), Position(xpos=-1, ypos=1), Position(xpos=-1, ypos=0)
                    ]
                    shifts.extend(shiftsArray)
                else:
                    #gorny w lancuchu
                    shiftsArray = [
                        Position(xpos=0, ypos=-1), Position(xpos=1, ypos=-1), Position(xpos=1, ypos=0),
                        Position(xpos=0, ypos=1), Position(xpos=-1, ypos=0), Position(xpos=-1, ypos=-1)
                    ]
                    shifts.extend(shiftsArray)
            elif distance == 2:
                if position.x % 2 == 0:
                    # dolny w lancuchu
                    shiftsArray = [
                        Position(xpos=-2, ypos=-1), Position(xpos=-1, ypos=-1), Position(xpos=0, ypos=-2),
                        Position(xpos=1, ypos=-1), Position(xpos=2, ypos=-1), Position(xpos=2, ypos=0),
                        Position(xpos=2, ypos=1), Position(xpos=1, ypos=2), Position(xpos=0, ypos=2),
                        Position(xpos=-1, ypos=2), Position(xpos=-2, ypos=1), Position(xpos=-2, ypos=0)
                    ]
                    shifts.extend(shiftsArray)
                else:
                    # gorny w lancuchu
                    shiftsArray = [
                        Position(xpos=-2, ypos=-1), Position(xpos=-1, ypos=-2), Position(xpos=0, ypos=-2),
                        Position(xpos=1, ypos=-2), Position(xpos=2, ypos=-1), Position(xpos=2, ypos=0),
                        Position(xpos=2, ypos=1), Position(xpos=1, ypos=1), Position(xpos=0, ypos=2),
                        Position(xpos=-1, ypos=1), Position(xpos=-2, ypos=1), Position(xpos=-2, ypos=0)
                    ]
                    shifts.extend(shiftsArray)
        pomPosition = None
        for sh in shifts:
            pomPosition = Position(xpos=position.x + sh.x, ypos=position.y + sh.y)
            if self.positionOnBoard(pomPosition):
                result.append(pomPosition)
        return result

    def getHuman(self):
        humanList = [ org for org in self.organisms if type(org) is Human ]
        if len(humanList) > 0:
            return humanList[0]
        return None

    def getNearestSosnowskiHogweed(self, org):
        sosnowskiHogweedList = [ org for org in self.organisms if type(org) is SosnowskiHogweed ]
        if len(sosnowskiHogweedList) > 0:
            odl = 1000
            barszcz = None
            for b in sosnowskiHogweedList:
                pom = org.position.distance(b.position)
                if pom < odl:
                    barszcz = b
                    odl = pom
            return barszcz
        return None

    def __str__(self):
        result = ""
        for y in range(0, self.boardY):
            for x in range(0, self.boardX):
                org = self.getOrganismFromPosition(Position(xpos=x, ypos=y))
                if org:
                    result += str(org.color.value) + " "
                else:
                    result += "_ "
            result += "\n"
        return result

