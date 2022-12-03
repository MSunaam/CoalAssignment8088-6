from collections import deque
from Supporitng_Functions import checkRegister, returnDecimal, checkMemory, flags, checkBinaryString


# Support
def printFlags():
    flags.printFlags()


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


# Support
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
    deq = deque(values)
    deq.rotate(times)
    register.inputList(list(deq))


def shr(rm, times, isMemory):
    # Shift the Register/Memory right times times
    # If times is negative use SHL
    if times < 0:
        shl(rm, abs(times), isMemory)
    if not isMemory:
        # rm is register
        check, register = checkRegister(rm)
        if not check:
            print('Register Incorrect')
            return
        # Register Correct
        # Get Register Values
        values = register.getData()
        # Using Deque because pop has O(1) complexity

        deq = deque(values)
        for x in range(times):
            if x == times - 1:
                # Last Iteration Store bit in CF
                flags.CF(deq[register.size - 1])
            deq.pop()
            deq.appendleft(0)
        register.inputList(list(deq))
    else:
        # rm is memory
        check, memory = checkMemory(rm)
        if not check:
            # rm is incorrect memory
            print("Memory out of range")
            return
        else:
            # Correct memory
            # Using deque because of less complexity
            deq = deque(memory.array)
            for x in range(times):
                if x == times - 1:
                    # Last Iteration store the bit in CF
                    flags.CF(memory.array[7])
                deq.pop()
                deq.appendleft(0)
            memory.array = list(deq)


def shl(rm, times, isMemory):
    # Shift the Register/Memory left times times
    # If times is negative use SHR
    if times < 0:
        shr(rm, abs(times), isMemory)
    if not isMemory:
        # rm is register
        check, register = checkRegister(rm)
        if not check:
            print('Register Incorrect')
            return
        # Register Correct
        # Get Register Values
        values = register.getData()
        # Using Deque because pop has O(1) complexity

        deq = deque(values)
        for x in range(times):
            if x == times - 1:
                # Last Iteration Store bit in CF
                flags.CF(deq[0])
            deq.popleft()
            deq.append(0)
        register.inputList(list(deq))
    else:
        # rm is memory
        check, memory = checkMemory(rm)
        if not check:
            # rm is incorrect memory
            print("Memory out of range")
            return
        else:
            # Correct memory
            # Using deque because of less complexity
            deq = deque(memory.array)
            for x in range(times):
                if x == times - 1:
                    # Last Iteration store the bit in CF
                    flags.CF(deq[0])
                deq.popleft()
                deq.append(0)
            memory.array = list(deq)


# Support
def setBitwise(register, binaryString):
    # Check if register correct
    check, register = checkRegister(register)
    if not check:
        print("Register Incorrect")
        return
    # Register Correct
    # Check binaryString
    if not checkBinaryString(binaryString):
        # Binary String Invalid
        print("The Binary expression is invalid")
        return False, None, None
    # Check if binary string greater than register size
    if len(binaryString) > register.size:
        binaryString = binaryString[-register.size:]
        # Checked in MASM

    # Check if length of binary string is smaller than register size
    if len(binaryString) < register.size:
        app = register.size - len(binaryString)
        binaryString = '0' * app + binaryString

    return True, binaryString, register


def AND(register, binaryString):
    # Set binary string and validate
    check, binaryString, register = setBitwise(register, binaryString)
    # check
    if not check:
        return
    # Get Register Values
    values = register.getData()
    # Take AND
    for x in range(register.size):
        values[x] = (values[x] & int(binaryString[x], 2))

    # Set Register Values
    register.inputList(values)


def OR(register, binaryString):
    # Set binary string and validate
    check, binaryString, register = setBitwise(register, binaryString)
    # check
    if not check:
        return
    # Get Register Values
    values = register.getData()
    # Take AND
    for x in range(register.size):
        values[x] = (values[x] | int(binaryString[x], 2))

    # Set Register Values
    register.inputList(values)
