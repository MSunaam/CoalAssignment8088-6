from commands import *
from Register_Instances import *
from Memory_Instances import *
from MachineCode import MachineCode

machineCode = MachineCode()

AX.input(5)
moveMemReg(machineCode, 'ax', 'F')
mem['F'].printMemory()

machineCode.print()
