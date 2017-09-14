from .Animal import Animal


class Wolf(Animal):

    def __init__(self, animal=None, position=None, world=None):
        super(Wolf, self).__init__(animal, position, world)

    def clone(self):
        return Wolf(self, None, None)

    def initParam(self):
        self.power = 9
        self.initiative = 5
