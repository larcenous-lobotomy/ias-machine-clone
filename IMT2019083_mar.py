from IMT2019083_pc import *

class MAR:

    def __init__(self, pc):
        self.pc = pc
        self.address = self.pc.get_address()

    def set_address(self, new_address):
        self.address = new_address

    def get_address(self):
        return self.address