from Register_Instances import *


# Increments Register

def inc(register):
    if register in Reg.keys():
        register = Reg[register]
    elif register in SubReg.keys():
        register = SubReg[register]
    else:
        print("Error: Register does not exist")
        return

    value = register.getData()
    value = ''.join(map(str, value))
    value = int(value, 2)
    register.input(value + 1)
