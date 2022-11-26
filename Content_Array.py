def convertToBinary(value, size=16):
    # Default argument 16 for whole register
    if size == 16 or size == 8:
        binaryy(0)
        # Initialize the array with 0s

    def input(self, value):
        # 16-bits input into X
        self.content = convertToBinary(value)

    def inputH(self, value):
        # 8-bits input into Higher(H)
        for x in range(8):
            self.content[x] = convertToBinary(value, 8)[x]
            # This will change only the first 8-bits

    def inputL(self, value):
        # 8-bits input into Lower(L)
        for x in range(8, 16):
            self.content[abs(x)] = convertToBinary(value, 8)[abs(x - 8)]
            # Content array needs to be accessed from 8 to 15 but convertToBinary needs to accessed from 0 to 7

    def swapHL(self):
        # For helping swap Higher and Lower for MOV commands
        # Save Higher in temp
        tempH = []
        for x in range(0, 8):
            tempH.append(self.content[x])
        # Put lower(8 to 15) into Higher(0 to 7)
        for x in range(8, 16):
            self.content[abs(x - 8)] = self.content[x]
        # Put tempH into lower(8 to 16)
        for x in range(8, 16):
            self.content[x] = tempH[abs(x - 8)]

    def getLow(self):
        # Get the lower part of the array
        return [self.content[x] for x in range(8, 16)]

    def getHigh(self):
        # Get the higher part of the array
        return [self.content[x] for x in range(8)]

    def print(self):
        # Temp function to check Array (Testing)
        print(self.content)


class Content_Array_16(Content_Array):
    # This array is for creating 16-bit registers like CS and DS
    # In such registers it is not allowed to access 8-bits low or high
    def inputH(self, value):
        pass

    def inputL(self, value):
        pass

    def swapHL(self):
        pass

    def getLow(self):
        pass

    def getHigh(self):
        pass
