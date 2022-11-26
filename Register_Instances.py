from Register import Register
from Register import FlagsReg

AX = Register("ax", True)
BX = Register('bx', True)
CX = Register('cx', True)
DX = Register('dx', True)
DS = Register('ds', False)
CS = Register('cs', False)
ES = Register('es', False)
Flag = FlagsReg()

Reg = {'ax': AX, 'bx': BX, 'cx': CX, 'dx': DX, 'ds': DS, 'cs': CS, 'es': ES}
subRegHigh = {'ah': AX, 'bh': BX, 'ch': CX, 'dh': DX}
subRegLow = {'al': AX, 'bl': BX, 'cl': CX, 'dl': DX}
