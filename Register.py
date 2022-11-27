from Content_Array import Content_Array
from Content_Array import Content_Array_16
from Content_Array import convertToBinary


class Register:
    def __init__(self, name, enableLowHigh):
        self.name = name
        self.size = 16
        self.setEnableLowHigh = enableLowHigh
        # Enable low high will determine if the register allows 8-bit access
        if enableLowHigh:
            # 8-bit access allowed
            self.content = Content_Array()
            self.lowerSubReg = subRegister(self.name[0] + "L", True, self.inputLow, self.getLow)
            self.higherSubReg = subRegister(self.name[0] + "H", False, self.inputHigh, self.getHigh)

        else:
            self.content = Content_Array_16()

    def printContent(self):
        print(self.content.getData())

    def input(self, values):
        # Input 16-bits
        self.content.input(values)

    def getData(self):
        # Return contents
        return self.content.getData()

    def inputHigh(self, values):
        # For setting High
        self.content.inputH(values)

    def getHigh(self):
        # For getting Higher 8-bits
        return self.content.getHigh()

    def inputLow(self, value):
        # For input low 8-bits
        self.content.inputL(value)

    def getLow(self):
        # For getting low 8-bits
        return self.content.getLow()


class subRegister:
    def __init__(self, name, low, inputFunc, outputFunc):
        self.name = name
        self.size = 8
        self.isLow = low
        self.input = inputFunc
        self.output = outputFunc
        # It has size of 8-bits

    def input(self, values):
        self.input(values)

    def getData(self):
        return self.output()


class FlagsReg:
    def __init__(self):
        self.content = Content_Array_16()
        # Only lower 4-bits are used for the flags CF,OF,ZF and SF

    def SF(self, setFlag):
        self.content.SF(setFlag)

    def OF(self, setFlag):
        self.content.OF(setFlag)

    def ZF(self, setFlag):
        self.content.ZF(setFlag)

    def CF(self, setFlag):
        self.content.CF(setFlag)
