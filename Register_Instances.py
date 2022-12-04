from Register import Register, FlagsReg

# We have 8 16-bit Registers and 4 lower registers and 4 higher registers

AX = Register('ax', True, 0)  # 000
AH = AX.higherSubReg  # 000
AL = AX.lowerSubReg  # 100
BX = Register('bx', True, 1)  # 001
BH = BX.higherSubReg  # 001
BL = BX.lowerSubReg  # 101
CX = Register('cx', True, 2)  # 010
CH = CX.higherSubReg  # 010
CL = CX.lowerSubReg  # 110
DX = Register('dx', True, 3)  # 011
DH = DX.higherSubReg  # 011
DL = DX.lowerSubReg  # 111

DS = Register('ds', False, 4)  # 100
CS = Register('cs', False, 5)  # 101
SS = Register('ss', False, 6)  # 110
ES = Register('es', False, 7)  # 111

Reg = {'ax': AX, 'bx': BX, 'cx': CX, 'dx': DX, 'ds': DS, 'cs': CS, 'ss': SS, 'es': ES}

SubReg = {'ah': AH, 'al': AL, 'bh': BH, 'bl': BL, 'ch': CH, 'cl': CL, 'dh': DH, 'dl': DL}
