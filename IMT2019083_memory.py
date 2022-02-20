from IMT2019083_aux import *

class Memory:

    def __init__(self):
        self.arrays = [] #memory arrays each of 40-bit
        try:
            memory_input = open("memory.txt", "r")
            while True:
                line = memory_input.readline()
                if not line:
                    break
                else:
                    self.arrays.append(str(line))
            memory_input.close()

        except FileNotFoundError:
            print("FileNotFoundError: No such memory input file can be traced.")

    def set(self, address, newdata):
        self.arrays[unsign_to_dec(address)] = newdata
        self.copyalltomemory()

    def get(self, address):
        return self.arrays[unsign_to_dec(address)]

    def copyalltomemory(self):
        memory_text = open("memory.txt", "w+")
        memory_text.truncate(0)
        memory_text.close()
        memory_text = open("memory.txt", "w+")
        for arr in self.arrays:
            memory_text.write(arr)

    def printall(self):
	    for arr in self.arrays:
		    print(arr)