from Register_Instances import *
from Supporitng_Functions import checkRegister, returnDecimal


# Increments Register

def inc(register):
    # If reg is full inc will make it 0
    # Check if register exists and then assign register object
    correctReg, register = checkRegister(register)
    if not correctReg:
        print("Register does not Exist")
        return

    # Get value of register and convert to decimal
    value = returnDecimal(register)
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
    check, register = checkRegister(register)

    if not check:
        print("Register does not exist")
        return

    # Get value of register and convert to decimal
    value = returnDecimal(register)
    # Increment Decimal Value
    value = value - 1
    registerSize = register.size
    # For getting Maximum value of the register
    if value >= 2 ** registerSize:
        value -= 2 ** registerSize

    register.input(value)
