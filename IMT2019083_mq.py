
class MQ:

    def __init__(self):
        self.data = ""

    def set(self, newdata):
        self.data = newdata

    def get(self):
        return self.data