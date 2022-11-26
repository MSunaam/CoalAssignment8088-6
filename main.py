from Register import Register
from Register import FlagsReg
from Supporitng_Functions import stringToList

AX = Register("ax", True)
BX = Register('bx', True)
CX = Register('cx', True)
DX = Register('dx', True)
DS = Register('ds', False)
CS = Register('cs', False)
ES = Register('es', False)
Flag = FlagsReg()

Reg = {'ax': AX, 'bx': BX, 'cx': CX, 'dx': DX, 'ds': DS, 'cs': CS, 'es': ES}

command = input("Please enter assembly command\n")
command = command.lower()
commandList = stringToList(command)
print(commandList)
