from Content_Array import Content_Array
from Content_Array import Content_Array_16


class Register:
    def __init__(self, name, enableLowHigh):
        self.registerLowHigh = enableLowHigh
        # For future reference to check if register allows accessing low and high or not
        self.name = name
        if enableLowHigh:
            self.content = Content_Array()
            # Allows access to individual 8-bits
            self.higherSubReg = subRegister(name[0] + 'H', self.content.getHigh())
            self.lowerSubReg = subRegister(name[0] + 'L', self.content.getLow())
        else:
            self.content = Content_Array_16()
            # Does not allow access to individual 8-bits

    def getLow(self):
        # Get the content of the lower Part
        if self.registerLowHigh:
            # 8-bit accessible register
            return self.lowerSubReg.getData()
        else:
            print("This Register does not support access of Lower 8-bits")

    def getHigh(self):
        # Get the content of the higher Part
        if self.registerLowHigh:
            # 8-bit accessible register
            return self.higherSubReg.getData()
        else:
            print("This Register does not support access of higher 8-bits")

    def setLow(self, values):
        # Set the content of the lower Part
        if self.registerLowHigh:
            # 8-bit accessible register
            # update the content array as well
            self.content.inputL(values)
            # This approach used because content array will automatically convert to binary and store in lower 8-bits
            # Also validation will be done
            self.lowerSubReg.setData(self.content.getLow())
        else:
            print("This Register does not support access of lower 8-bits")

    def setHigh(self, values):
        # Set the content of the higher Part
        if self.registerLowHigh:
            # 8-bit accessible register
            # update the content array as well
            self.content.inputH(values)
            # This approach used because content array will automatically convert to binary and store in higher 8-bits
            # Also validation will be done
            self.higherSubReg.setData(self.content.getHigh())
        else:
            print("This Register does not support access of higher 8-bits")

    def setData(self, values):
        # Set the data of the whole register
        self.content.input(values)
        # Now change the values of subRegisters if exist
        if self.registerLowHigh:
            # SubRegisters Exist
            self.higherSubReg.setData(self.content.getHigh())
            self.lowerSubReg.setData(self.content.getLow())

    def getData(self):
        return self.content.getData()

    def printContent(self):
        self.content.print()


class subRegister:

    # This class is for storing lower and higher parts of Registers
    def __init__(self, name, values=None):
        # Initialize the subRegister
        if values is None:
            values = []
        self.array = values
        self.name = name

    def getData(self):
        # Get the data from sub-Register
        return self.array

    def setData(self, values):
        # Set the values
        self.array = values
