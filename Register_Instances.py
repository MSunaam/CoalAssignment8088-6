from Register import Register

# We have 8 16-bit Registers and 4 lower registers and 4 higher registers

AX = Register('ax', True)
AH = AX.higherSubReg
AL = AX.lowerSubReg
BX = Register('bx', True)
BH = BX.higherSubReg
BL = BX.lowerSubReg
CX = Register('cx', True)
CH = CX.higherSubReg
CL = CX.lowerSubReg
DX = Register('dx', True)
DH = DX.higherSubReg
DL = DX.lowerSubReg

DS = Register('ds', False)
CS = Register('cs', False)
SS = Register('ss', False)
ES = Register('es', False)

Reg = {'ax': AX, 'bx': BX, 'cx': CX, 'dx': DX, 'ds': DS, 'cs': CS, 'ss': SS, 'es': ES}

SubReg = {'ah': AH, 'al': AL, 'bh': BH, 'bl': BL, 'ch': CH, 'cl': CL, 'dh': DH, 'dl': DL}
