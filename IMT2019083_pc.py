
class PC:

    def __init__(self):
        self.address = "0"*12

    def set_address(self, new_address):
        self.address = new_address

    def get_address(self):
        return self.address    
