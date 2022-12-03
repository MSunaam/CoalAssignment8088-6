from Register_Instances import *
from Memory_Instances import *

# Register to Store the State of the Flags
flags = FlagsReg()


def checkRegister(register):
    # Check if register exists
    if register in Reg.keys():
        register = Reg[register]
        return True, register
    elif register in SubReg.keys():
        register = SubReg[register]
        return True, register
    else:
        return False, None


def checkMemory(memory):
    # Check if memory is in range
    if memory in mem.keys():
        memory = mem[memory]
        return True, memory
    else:
        return False, None


def returnDecimal(register):
    # Returns the register's decimal value passed
    value = register.getData()
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
