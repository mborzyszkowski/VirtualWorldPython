class ActionLogger:

    def __init__(self):
        self.actionDescriptions=[]

    def addDescriptions(self, description):
        self.actionDescriptions.append(description)

    def __str__(self):
        return "\n".join(self.actionDescriptions)

    def clear(self):
        self.actionDescriptions=[]

    def isEmpty(self):
        return not self.actionDescriptions
