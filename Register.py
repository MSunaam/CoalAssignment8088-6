from Content_Array import Content_Array
from Content_Array import Content_Array_16


class Register:
    def __init__(self, name, enableLowHigh):
        self.registerLowHigh = enableLowHigh
        # For future reference to check if register allows accessing low and high or not
        self.low = None
        # If register allows accessing low and high; store low in low
        self.high = None
        # If register allows accessing low and high; store high in high
        self.name = name
        if enableLowHigh:
            self.content = Content_Array()
            # Allows access to individual 8-bits
        else:
            self.content = Content_Array_16()
            # Does not allow access to individual 8-bits

    def getLow(self):
        # Get Low Contents
        if self.registerLowHigh:
            self.low = self.content.getLow()
            return self.low
        else:
            print("Register Error: Register does not allow accessing Low and High")

    def getHigh(self):
        # Get High Contents
        if self.registerLowHigh:
            self.high = self.content.getHigh()
            return self.high
        else:
            print("Register Error: Register does not allow accessing Low and High")

    def getData(self):
        # Get Register Contents
        return self.content.getData()

    def input(self, value):
        # Update Register Contents
        self.content.input(value)

    def inputLow(self, value):
        # Update Low Contents
        if self.registerLowHigh:
            self.content.inputL(value)
        else:
            print("Register Error: Register does not allow accessing Low and High")

    def inputHigh(self, value):
        # Update High Contents
        if self.registerLowHigh:
            self.content.inputH(value)
        else:
            print("Register Error: Register does not allow accessing Low and High")
