from Content_Array import Content_Array
from Content_Array import Content_Array_16
from Content_Array import convertToBinary


class Register:
    def __init__(self, name, enableLowHigh, code):
        self.code = str(bin(code))[2:].zfill(3)
        self.name = name
        self.size = 16
        self.setEnableLowHigh = enableLowHigh
        # Enable low high will determine if the register allows 8-bit access
        if enableLowHigh:
            # 8-bit access allowed
            self.type = 1  # General Purpose Register
            self.content = Content_Array()
            self.lowerSubReg = subRegister(self.name[0] + "L", True, self.inputLow, self.getLow, self.inputListLow,
                                           str(bin(code + 4))[2:].zfill(3))
            self.higherSubReg = subRegister(self.name[0] + "H", False, self.inputHigh, self.getHigh, self.inputListHigh,
                                            str(bin(code))[2:].zfill(3))

        else:
            self.content = Content_Array_16()
            self.type = 0  # Segment Register

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

    def inputList(self, inputList):
        self.content.content = inputList

    def inputListLow(self, inputList):
        for x in range(8, 16):
            self.content.content[x] = inputList[x - 8]

    def inputListHigh(self, inputList):
        for x in range(8):
            self.content.content[x] = inputList[x]

    def getCode(self):
        return self.code


class subRegister:
    def __init__(self, name, low, inputFunc, outputFunc, inputList, code):
        self.code = code
        self.name = name
        self.size = 8
        self.isLow = low
        self.input = inputFunc
        self.output = outputFunc
        self.inputList = inputList
        # It has size of 8-bits

    def getCode(self):
        return self.code

    def inputList(self, inputList):
        self.inputList(inputList)

    def input(self, values):
        self.input(values)

    def getData(self):
        return self.output()

    def printContent(self):
        print(self.getData())


class FlagsReg:
    def __init__(self):
        self.content = Content_Array_16()
        # Only lower 4-bits are used for the flags CF,OF,ZF and SF

    def printFlags(self):
        print(
            f"CF: {self.content.content[12]}\tZF: {self.content.content[13]}\tOF: {self.content.content[14]}\tSF: {self.content.content[15]}")

    def SF(self, setFlag):
        self.content.SF(setFlag)

    def OF(self, setFlag):
        self.content.OF(setFlag)

    def ZF(self, setFlag):
        self.content.ZF(setFlag)

    def CF(self, setFlag):
        self.content.CF(setFlag)
