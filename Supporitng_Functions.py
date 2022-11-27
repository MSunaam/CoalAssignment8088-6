from Register_Instances import *


def checkRegister(register):
    # Check if register exists
    if register in Reg.keys():
        register = Reg[register]
        return True, register
    elif register in SubReg.keys():
        register = SubReg.keys()
        return True, register
    else:
        return False, None


def returnDecimal(register):
    # Returns the register's decimal value passed
    value = register.getData()
    value = ''.join(map(str, value))
    value = int(value, 2)
    return value
