from Content_Array import convertToBinary


class Memory_Array:
    # To initialize memory arrays
    def __init__(self):
        self.array = convertToBinary(0, 8, 'Memory')
        # Initialize the array with 0's

    def input(self, value):
        self.array = convertToBinary(value, 8, "Memory")

    def inputList(self, inputList):
        self.array = inputList

    def getData(self):
        return self.array

    def printMemory(self):
        print(self.array)
