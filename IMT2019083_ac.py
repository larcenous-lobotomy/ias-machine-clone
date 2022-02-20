#40 bit accumulator
class AC:

    def __init__(self):
        self.data = ""

    def set(self, newdata):
        self.data = newdata

    def get(self):
        return self.data