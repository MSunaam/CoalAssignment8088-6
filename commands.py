from Register_Instances import *


# Increments Register

def inc(register):
    # If reg is full inc will make it 0
    # Check if register exists and then assign register object
    if register in Reg.keys():
        register = Reg[register]
    elif register in SubReg.keys():
        register = SubReg[register]
    else:
        print("Error: Register does not exist")
        return

    # Get value of register and convert to decimal
    value = register.getData()
    value = ''.join(map(str, value))
    value = int(value, 2)
    # Increment Decimal Value
    value = value + 1
    registerSize = register.size
    # For getting Maximum value of the register
    if value >= 2 ** registerSize:
        value -= 2 ** registerSize

    register.input(value)


def dec(register):
    # This will decrement the value of the register by 1
    # If reg is empty inc will make it FFFFFFFFFFFFFFFFF
    # Check if register exists and then assign register object
    if register in Reg.keys():
        register = Reg[register]
    elif register in SubReg.keys():
        register = SubReg[register]
    else:
        print("Error: Register does not exist")
        return

    # Get value of register and convert to decimal
    value = register.getData()
    value = ''.join(map(str, value))
    value = int(value, 2)
    # Increment Decimal Value
    value = value - 1
    registerSize = register.size
    # For getting Maximum value of the register
    if value >= 2 ** registerSize:
        value -= 2 ** registerSize

    register.input(value)
