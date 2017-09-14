from .Plant import Plant


class Dandelion(Plant):
    def __init__(self, plant=None, position=None, world=None):
        super(Dandelion, self).__init__(plant, position, world)

    def clone(self):
        return Dandelion(self, None, None)

    def initParam(self):
        self.power = 0
        self.initiative = 0
        self.reproductionProbability = 30

    def move(self):
        result = []
        for i in range(0,3):
            result.extend(super(Dandelion, self).move())
            if result:
                break
        return result
