class MachineCode:
    def __init__(self):
        self.opcode = ''
        self.dBit = ''
        self.wBit = ''
        self.rm1 = ''
        self.rm2 = ''
        self.disp = ''
        self.imm = ''

    def print(self):
        print(f"{self.opcode}{self.dBit}{self.wBit} {self.rm1} {self.rm2} {self.disp} {self.imm}")
