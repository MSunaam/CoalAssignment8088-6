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


# def AND(register, binaryString):
#     # Set binary string and validate
#     check, binaryString, register = setBitwise(register, binaryString)
#     # check
#     if not check:
#         return
#     # Get Register Values
#     values = register.getData()
#     # Take AND
#     for x in range(register.size):
#         values[x] = (values[x] & int(binaryString[x], 2))
#
#     # Set Register Values
#     register.inputList(values)

def AND(mode, rm1='', rm2='', binaryString=''):
    # rm1 will always be reg and rm2 may be reg or mem
    if mode == 1 or mode == 2:
        check, register = checkRegister(rm1)
        if not check:
            print("Register Incorrect")
            return
        check, memory = checkMemory(rm2)
        if not check:
            print("Memory Out of Range")
            return

        # Get register values
        valuesReg = register.getData()
        # Get Memory values
        # Memory Size is always 8
        valuesMem = memory.getData()

        if mode == 1:
            # mode = 1 = REG, Mem
            if register.size == 8:
                for x in range(8):
                    valuesReg[x] = valuesReg[x] & valuesMem[x]
                register.inputList(valuesReg)
                return
            else:
                # Register Size = 16
                for x in range(8):
                    valuesMem.insert(0, 0)
                for x in range(16):
                    valuesReg[x] = valuesReg[x] & valuesMem[x]
                register.inputList(valuesReg)
                return
        elif mode == 2:
            # mode = 2 = mem, Reg
            if register.size == 16:
                valuesReg = valuesReg[-8:]
            # Take AND
            for x in range(8):
                valuesMem[x] = valuesMem[x] & valuesReg[x]
            memory.inputList(valuesReg)
            return
    elif mode == 3:
        # mode = 3 = Reg, Reg
        check1, reg1 = checkRegister(rm1)
        check2, reg2 = checkRegister(rm2)
        if not check2 and check1:
            print("Registers Incorrect")
            return
        valuesReg1 = reg1.getData()
        valuesReg2 = reg2.getData()
        if reg1.size == 16 and reg2.size == 16:
            for x in range(16):
                valuesReg1[x] = valuesReg1[x] & valuesReg2[x]
        elif reg1.size == 8 and reg2.size == 8:
            for x in range(8):
                valuesReg1[x] = valuesReg1[x] & valuesReg2[x]
        elif reg1.size == 8 and reg2.size == 16:
            valuesReg2 = valuesReg2[-8:]
            for x in range(8):
                valuesReg1[x] = valuesReg1[x] & valuesReg2[x]
        elif reg1.size == 16 and reg2.size == 8:
            for x in range(8):
                valuesReg2.insert(0, 0)
            for x in range(16):
                valuesReg1[x] = valuesReg1[x] & valuesReg2[x]
        reg1.inputList(valuesReg1)
        return
    elif mode == 4:
        # mode = 4 = mem, imm
        check, memory = checkMemory(rm1)
        if not check:
            print("Memory Incorrect")
            return
        # Get mem value
        valueMem = memory.getData()
        # Pad zeros
        if len(binaryString) < 8:
            binaryString = '0' * (8 - len(binaryString)) + binaryString
        elif len(binaryString) > 8:
            binaryString = binaryString[-8:]
        # Take AND
        for x in range(8):
            valueMem[x] = valueMem[x] & int(binaryString[x])
        memory.inputList(valueMem)
        return
    elif mode == 5:
        # mode = 5 = reg, imm
        check, register = checkRegister(rm1)
        if not check:
            print("Register Incorrect")
            return
        # Get mem value
        valueReg = register.getData()
        # Pad zeros
        if len(binaryString) < register.size:
            binaryString = '0' * (register.size - len(binaryString)) + binaryString
        elif len(binaryString) > register.size:
            binaryString = binaryString[-register.size:]
        # Take AND
        for x in range(register.size):
            valueReg[x] = valueReg[x] & int(binaryString[x])
        register.inputList(valueReg)
        return


def OR(mode, rm1='', rm2='', binaryString=''):
    # rm1 will always be reg and rm2 may be reg or mem
    if mode == 1 or mode == 2:
        check, register = checkRegister(rm1)
        if not check:
            print("Register Incorrect")
            return
        check, memory = checkMemory(rm2)
        if not check:
            print("Memory Out of Range")
            return

        # Get register values
        valuesReg = register.getData()
        # Get Memory values
        # Memory Size is always 8
        valuesMem = memory.getData()

        if mode == 1:
            # mode = 1 = REG, Mem
            if register.size == 8:
                for x in range(8):
                    valuesReg[x] = valuesReg[x] | valuesMem[x]
                register.inputList(valuesReg)
                return
            else:
                # Register Size = 16
                for x in range(8):
                    valuesMem.insert(0, 0)
                for x in range(16):
                    valuesReg[x] = valuesReg[x] | valuesMem[x]
                register.inputList(valuesReg)
                return
        elif mode == 2:
            # mode = 2 = mem, Reg
            if register.size == 16:
                valuesReg = valuesReg[-8:]
            # Take AND
            for x in range(8):
                valuesMem[x] = valuesMem[x] | valuesReg[x]
            memory.inputList(valuesReg)
            return
    elif mode == 3:
        # mode = 3 = Reg, Reg
        check1, reg1 = checkRegister(rm1)
        check2, reg2 = checkRegister(rm2)
        if not check2 and check1:
            print("Registers Incorrect")
            return
        valuesReg1 = reg1.getData()
        valuesReg2 = reg2.getData()
        if reg1.size == 16 and reg2.size == 16:
            for x in range(16):
                valuesReg1[x] = valuesReg1[x] | valuesReg2[x]
        elif reg1.size == 8 and reg2.size == 8:
            for x in range(8):
                valuesReg1[x] = valuesReg1[x] | valuesReg2[x]
        elif reg1.size == 8 and reg2.size == 16:
            valuesReg2 = valuesReg2[-8:]
            for x in range(8):
                valuesReg1[x] = valuesReg1[x] | valuesReg2[x]
        elif reg1.size == 16 and reg2.size == 8:
            for x in range(8):
                valuesReg2.insert(0, 0)
            for x in range(16):
                valuesReg1[x] = valuesReg1[x] | valuesReg2[x]
        reg1.inputList(valuesReg1)
        return
    elif mode == 4:
        # mode = 4 = mem, imm
        check, memory = checkMemory(rm1)
        if not check:
            print("Memory Incorrect")
            return
        # Get mem value
        valueMem = memory.getData()
        # Pad zeros
        if len(binaryString) < 8:
            binaryString = '0' * (8 - len(binaryString)) + binaryString
        elif len(binaryString) > 8:
            binaryString = binaryString[-8:]
        # Take AND
        for x in range(8):
            valueMem[x] = valueMem[x] | int(binaryString[x])
        memory.inputList(valueMem)
        return
    elif mode == 5:
        # mode = 5 = reg, imm
        check, register = checkRegister(rm1)
        if not check:
            print("Register Incorrect")
            return
        # Get mem value
        valueReg = register.getData()
        # Pad zeros
        if len(binaryString) < register.size:
            binaryString = '0' * (register.size - len(binaryString)) + binaryString
        elif len(binaryString) > register.size:
            binaryString = binaryString[-register.size:]
        # Take AND
        for x in range(register.size):
            valueReg[x] = valueReg[x] | int(binaryString[x])
        register.inputList(valueReg)
        return
