from Content_Array import convertToBinary


class Memory_Array:
    # To initialize memory arrays
    def __init__(self, index):
        self.array = convertToBinary(0, 8, 'Memory')
        self.index = str(bin(index))[2:].zfill(3)
        # Initialize the array with 0's

    def getIndex(self):
        return self.index

    def input(self, value):
        self.array = convertToBinary(value, 8, "Memory")

    def inputList(self, inputList):
        self.array = inputList

    def getData(self):
        return self.array

    def printMemory(self):
        print(self.array)
