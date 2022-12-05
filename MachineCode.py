class MachineCode:
    def __init__(self):
        self.opcode = ''
        self.dBit = '0'
        self.wBit = '0'
        self.mod = '00'
        self.reg = '000'
        self.rm2 = '0000'
        self.imm = ''

    def print(self):
        print(
            f"{self.opcode} {self.dBit}{self.wBit} {self.mod} {self.reg} {self.rm2} {self.imm}\n")

    def returnCode(self):
        return f"{self.opcode} {self.dBit}{self.wBit} {self.mod} {self.reg} {self.rm2} {self.imm}\n"

    def clear(self):
        self.opcode = ''
        self.dBit = '0'
        self.wBit = '0'
        self.mod = '0'
        self.reg = '000'
        self.rm2 = '0000'
        self.imm = ''

    def setOpcode(self, string):
        self.opcode = string

    def setDBit(self, string):
        self.dBit = string

    def setWBit(self, string):
        self.wBit = string

    def setReg(self, string):
        self.reg = string

    def setRM2(self, string):
        self.rm2 = string

    def setDisp(self, string):
        self.disp = string

    def setImm(self, string):
        self.imm = string

    def setMode(self, string):
        self.mod = string
