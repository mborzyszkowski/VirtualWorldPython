from .Animal import Animal

class Sheep(Animal):

    def __init__(self, animal=None, position=None, world=None):
        super(Sheep, self).__init__(animal, position, world)

    def clone(self):
        return Sheep(self, None, None)

    def initParam(self):
        self.power = 4
        self.initiative = 4

