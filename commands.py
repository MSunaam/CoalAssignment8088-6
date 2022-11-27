from Register_Instances import *


# Increments Register

def inc(register):
    if register not in Reg:
        print("Register Error, Register does not exist")
        return

    value = register.getData()
    value = ''.join(map(str, value))
    value = int(value, 2)
    register.input(value + 1)
