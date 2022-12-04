from commands import *
from Register_Instances import *
from Memory_Instances import *
from MachineCode import MachineCode

machineCode = MachineCode()

inc(machineCode, 'A', True)
mem['A'].printMemory()
machineCode.print()
