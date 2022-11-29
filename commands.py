from Register_Instances import *
from collections import deque
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


def rol(register, times):
    if times > 0:
        rotate(register, -times)
    else:
        rotate(register, -times)


def ror(register, times):
    if times > 0:
        rotate(register, times)
    else:
        rotate(register, times)


def rotate(register, times):
    # If times is positive it will rotate right and if it is negative it will rotate left
    # Register values will be rotated right times times
    # Get Register value
    check, register = checkRegister(register)
    if not check:
        print("Invalid Register")
        return
    # Get register data
    values = register.getData()
    # If times greater than register size subtract checked on Masm
    if times > register.size:
        times = times - register.size
    deq = deque(register.content.content)
    deq.rotate(times)
    register.content.content = list(deq)
