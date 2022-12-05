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


from memory import Memory_Array

mem = {'0': Memory_Array(0),
       '1': Memory_Array(1),
       '2': Memory_Array(2),
       '3': Memory_Array(3),
       '4': Memory_Array(4),
       '5': Memory_Array(5),
       '6': Memory_Array(6),
       '7': Memory_Array(7),
       '8': Memory_Array(8),
       '9': Memory_Array(9),
       'A': Memory_Array(10),
       'B': Memory_Array(11),
       'C': Memory_Array(12),
       'D': Memory_Array(13),
       'E': Memory_Array(14),
       'F': Memory_Array(15),
       }
