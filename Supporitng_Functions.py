from Register_Instances import *
from Memory_Instances import *
from MachineCode import MachineCode

# Register to Store the State of the Flags
flags = FlagsReg()


def checkRegister(register, machineCode):
    # Check if register exists
    if register in Reg.keys():
        register = Reg[register]
        machineCode.setWBit('1')
        return True, register
    elif register in SubReg.keys():
        register = SubReg[register]
        machineCode.setWBit('0')
        return True, register
    else:
        return False, None


def checkMemory(memory, machineCode):
    # Check if memory is in range
    if memory in mem.keys():
        machineCode.setRM2(bin(int(memory, 16))[2:].zfill(4))
        memory = mem[memory]
        return True, memory
    else:
        return False, None


def returnDecimal(listValue):
    # Returns the register's decimal value passed
    value = listValue
    value = ''.join(map(str, value))
    value = int(value, 2)
    return value


def checkBinaryString(string):
    P = set(string)
    S = {'0', '1'}
    if P == S or P == {'1'} or P == {'0'}:
        return True
    else:
        return False
