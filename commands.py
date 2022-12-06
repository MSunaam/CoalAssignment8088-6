from collections import deque
from Supporitng_Functions import checkRegister, returnDecimal, checkMemory, flags


# Opcode = 10
def movRegReg(machineCode, reg1, reg2):
    # Get opcode
    machineCode.setOpcode('1010')
    # Set mode
    machineCode.setMode('1')
    # Check registers
    check1, reg1 = checkRegister(reg1, machineCode)
    check2, reg2 = checkRegister(reg2, machineCode)
    if not reg1 and not reg2:
        print('Invalid Registers')
        return
    if reg1.type == 0 and reg2.type == 0:
        # type 0 means segment register
        print('Cannot move from segment to segment')
        return 'Cannot move from segment to segment'

    # Get reg and rm for machine code
    machineCode.setReg(reg1.getCode())
    machineCode.setRM2(reg2.getCode())
    # Set Mode
    machineCode.setMode('1')
    # Set D-bit
    machineCode.setDBit('1')
    # Get value of reg2
    valuesReg2 = reg2.getData()
    # Insert into Reg1
    reg1.inputList(valuesReg2)


# Opcode = 11
def moveRegMem(machineCode, reg, mem):
    # Get Opcode
    machineCode.setOpcode('1011')
    # Set mod
    machineCode.setMode('0')
    # Set d bit to 1
    machineCode.setDBit('1')
    # Get and check reg
    check, register = checkRegister(reg, machineCode)
    if not check:
        print('Invalid Register')
        return
    # Check memory
    check, memory = checkMemory(mem, machineCode)
    if not check:
        print("invalid Memory")
        return
    # Get codes
    machineCode.setReg(register.getCode())
    # Get value of memory
    valueMem = memory.getData()
    # Convert memData to decimal
    value = returnDecimal(valueMem)
    # Input in reg
    register.input(value)


# Opcode = 12
def moveMemReg(machineCode, reg, mem):
    # Get Opcode
    machineCode.setOpcode('1100')
    # Set D-bit
    machineCode.setMode('0')
    # Set Mode
    machineCode.setMode('0')
    # Check register
    check, reg = checkRegister(reg, machineCode)
    if not check:
        print("Invalid Register")
        return
    # Get register code
    machineCode.setReg(reg.getCode())
    # Check memory
    check, mem = checkMemory(mem, machineCode)
    # Transfer Data
    value = returnDecimal(reg.getData())
    mem.input(value)


# Opcode = 13
def moveRegImm(machineCode, reg, imm):
    imm = int(imm)
    # Get Opcode
    machineCode.setOpcode('1101')
    # Set mode
    machineCode.setMode('1')
    # Check register
    check, register = checkRegister(reg, machineCode)
    if not check:
        print('Invalid Register')
        errorMsg = "Invalid Register"
        return errorMsg
    # Get register Code
    machineCode.setReg(register.getCode())
    # Get immediate data
    # Set imm
    data = bin((imm) if (imm) > 0 else (imm) + (1 << 8))[2:]
    data = data.zfill(8)
    machineCode.setImm(data)
    # Check if register with immediate data
    if imm > 2**register.size:
        return "Immediate data is too large for register"
    # Transfer to reg
    register.input(imm)
    return


# Opcode = 14
def movMemImm(machineCode, mem, imm):
    imm = int(imm)
    # Get Opcode
    machineCode.setOpcode('1111')
    # Set mode
    machineCode.setMode('0')
    # Get memory
    check, memory = checkMemory(mem, machineCode)
    if not check:
        print("Incorrect Memory")
        return
    # Get immediate data
    # Set imm
    data = bin(imm if imm > 0 else imm + (1 << 8))[2:]
    data = data.zfill(8)
    machineCode.setImm(data)
    # Transfer to mem
    memory.input(imm)
    return


# Support
def printFlags():
    flags.printFlags()


# Opcode  = 8
def inc(machineCode, rm, isMemory):
    # Set Opcode
    machineCode.setOpcode('1000')

    if not isMemory:
        # Set Mode
        machineCode.setMode('1')  # Mode =1 reg
        # rm is register
        # If reg is full inc will make it 0
        # Check if register exists and then assign register object
        correctReg, register = checkRegister(rm, machineCode)
        if not correctReg:
            print("Register does not Exist")
            return
        # Get Register code
        machineCode.setReg(register.getCode())
        # Get value of register and convert to decimal
        value = returnDecimal(register.getData())
        # Increment Decimal Value
        value = value + 1
        registerSize = register.size
        # For getting Maximum value of the register
        if value >= 2 ** registerSize:
            value -= 2 ** registerSize

        register.input(value)
    else:
        # rm is memory
        # set mode
        machineCode.setMode('0')  # mode = 0 memory
        correct, memory = checkMemory(rm, machineCode)
        # Get memory Value
        valueMem = memory.getData()
        # Get the value of the memory as a decimal
        value = returnDecimal(valueMem)
        # Increment value
        value += 1
        # For getting max value
        if value >= 2 ** 8:
            value -= 2 ** 8

        memory.input(value)


# Opcode = 9
def dec(machineCode, rm, isMemory):
    # This will decrement the value of the register by 1
    # If reg is empty inc will make it FFFFFFFFFFFFFFFFF
    # Set Opcode
    machineCode.setOpcode('1001')

    if not isMemory:
        # Set Mode
        machineCode.setMode('1')  # Mode =1 reg
        # rm is register
        # Check if register exists and then assign register object
        correctReg, register = checkRegister(rm, machineCode)
        if not correctReg:
            print("Register does not Exist")
            return
        # Get Register code
        machineCode.setReg(register.getCode())
        # Get value of register and convert to decimal
        value = returnDecimal(register.getData())
        # Decrement Decimal Value
        value = value - 1
        registerSize = register.size
        # For getting Maximum value of the register
        if value >= 2 ** registerSize:
            value -= 2 ** registerSize

        register.input(value)
    else:
        # rm is memory
        # set mode
        machineCode.setMode('0')  # mode = 0 memory
        correct, memory = checkMemory(rm, machineCode)
        # Get memory Value
        valueMem = memory.getData()
        # Get the value of the memory as a decimal
        value = returnDecimal(valueMem)
        # Decrement value
        value -= 1
        # For getting max value
        if value >= 2 ** 8:
            value -= 2 ** 8

        memory.input(value)


# Opcode = 6
def rol(machineCode, rm, times, isMemory):
    # Set immediateData
    imm = str(bin(times if times > 0 else times + (1 << 8)))[2:]
    imm = imm.zfill(8)
    machineCode.setImm(imm)
    # Set opcode
    machineCode.setOpcode('0110')

    if times > 0:
        rotate(machineCode, rm, -times, isMemory)
    else:
        rotate(machineCode, rm, -times, isMemory)


# Opcode = 7
def ror(machineCode, rm, times, isMemory):
    # Set immediateData
    imm = bin(times if times > 0 else times + (1 << 8))[2:]
    imm = imm.zfill(8)
    machineCode.setImm(imm)
    # Set opcode
    machineCode.setOpcode('0111')

    if times > 0:
        rotate(machineCode, rm, times, isMemory)
    else:
        rotate(machineCode, rm, times, isMemory)


# Support
def rotate(machineCode, rm, times, isMemory):
    # If times is positive it will rotate right and if it is negative it will rotate left
    # Register values will be rotated right times times

    if not isMemory:
        # rm is reg
        check, register = checkRegister(rm, machineCode)
        if not check:
            print("Invalid Register")
            return
        # set Reg
        machineCode.setReg(register.getCode())
        # set Mode
        machineCode.setMode('1')  # 1 = reg

        # Get register data
        values = register.getData()
        # If times greater than register size subtract checked on Masm
        if times > register.size:
            times = times - register.size
        deq = deque(values)
        deq.rotate(times)
        register.inputList(list(deq))
    else:
        # Memory
        # Set Mode
        machineCode.setMode('0')  # 0 = memory

        check, memory = checkMemory(rm, machineCode)

        # Get memory Value
        valueMem = memory.getData()

        if times > 8:
            times = times - 8
        deq = deque(valueMem)
        deq.rotate(times)
        memory.inputList(list(deq))


# Opcode = 3
def shr(machineCode, rm, times, isMemory):
    # Set Opcode
    machineCode.setOpcode('0011')
    # Set imm
    imm = bin(times if times > 0 else times + (1 << 8))[2:]
    imm = imm.zfill(8)
    machineCode.setImm(imm)
    # Shift the Register/Memory right times times
    # If times is negative use SHL
    if times < 0:
        shl(machineCode, rm, abs(times), isMemory)
    if not isMemory:
        # rm is register
        check, register = checkRegister(rm, machineCode)
        if not check:
            print('Register Incorrect')
            return
        # Register Correct
        # Set Register code
        machineCode.setReg(register.code)
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
        check, memory = checkMemory(rm, machineCode)
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


# Opcode = 4
def shl(machineCode, rm, times, isMemory):
    # Set Opcode
    machineCode.setOpcode('0100')
    # Set imm
    imm = bin(times if times > 0 else times + (1 << 8))[2:]
    imm = imm.zfill(8)
    machineCode.setImm(imm)
    # Shift the Register/Memory left times times
    # If times is negative use SHR
    if times < 0:
        shr(machineCode, rm, abs(times), isMemory)
    if not isMemory:
        # rm is register
        check, register = checkRegister(rm, machineCode)
        if not check:
            print('Register Incorrect')
            return
        # Register Correct
        # Set Register code
        machineCode.setReg(register.code)
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
        check, memory = checkMemory(rm, machineCode)
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


# Opcode = 0
def AND(mode, machineCode, rm1='', rm2='', binaryString=''):
    machineCode.setOpcode('0000')
    # rm1 will always be reg and rm2 may be reg or mem
    if mode == 1 or mode == 2:
        check, register = checkRegister(rm1, machineCode)
        if not check:
            print("Register Incorrect")
            return
        check, memory = checkMemory(rm2, machineCode)
        if not check:
            print("Memory Out of Range")
            return

        # Get register values
        valuesReg = register.getData()
        machineCode.setReg(register.getCode())
        # Get Memory values
        # Memory Size is always 8
        valuesMem = memory.getData()
        # Set Reg code
        machineCode.setReg(register.getCode())

        if mode == 1:
            # mode = 1 = REG, Mem
            machineCode.setMode('0')  # Mode 0 Memory
            machineCode.setDBit('1')
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
            machineCode.setMode('0')  # Mode 0 memory
            machineCode.setDBit('0')  # D bit 0 = Reg to RM
            if register.size == 16:
                valuesReg = valuesReg[-8:]
            # Take AND
            for x in range(8):
                valuesMem[x] = valuesMem[x] & valuesReg[x]
            memory.inputList(valuesMem)
            return
    elif mode == 3:
        # mode = 3 = Reg, Reg
        check1, reg1 = checkRegister(rm1, machineCode)
        check2, reg2 = checkRegister(rm2, machineCode)
        if not check2 and check1:
            print("Registers Incorrect")
            return
        # Set Reg Codes
        machineCode.setReg(reg1.getCode())
        machineCode.setRM2(reg2.getCode())
        machineCode.setDBit('1')
        machineCode.setMode('1')  # Mode 11 RM is Register
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
        check, memory = checkMemory(rm2, machineCode)
        if not check:
            print("Memory Incorrect")
            return
        # Set RM
        machineCode.setMode('0')  # Mode 0 memory

        # Get mem value
        valueMem = memory.getData()
        # Pad zeros
        if len(binaryString) < 8:
            binaryString = '0' * (8 - len(binaryString)) + binaryString
        elif len(binaryString) > 8:
            binaryString = binaryString[-8:]

        # set imm
        machineCode.setImm(binaryString)

        # Take AND
        for x in range(8):
            valueMem[x] = valueMem[x] & int(binaryString[x])
        memory.inputList(valueMem)
        return
    elif mode == 5:
        # mode = 5 = reg, imm
        check, register = checkRegister(rm1, machineCode)
        if not check:
            print("Register Incorrect")
            return
        # Set Reg
        machineCode.setReg(register.getCode())
        # Set mode
        machineCode.setMode('0')  # Mode not required
        # Get mem value
        valueReg = register.getData()
        # Pad zeros
        if len(binaryString) < register.size:
            binaryString = '0' * \
                (register.size - len(binaryString)) + binaryString
        elif len(binaryString) > register.size:
            binaryString = binaryString[-register.size:]
        # set imm
        machineCode.setImm(binaryString)

        # Take AND
        for x in range(register.size):
            valueReg[x] = valueReg[x] & int(binaryString[x])
        register.inputList(valueReg)
        return


# Opcode = 1
def OR(mode, machineCode, rm1='', rm2='', binaryString=''):
    machineCode.setOpcode('0001')
    # rm1 will always be reg and rm2 may be reg or mem
    if mode == 1 or mode == 2:
        check, register = checkRegister(rm1, machineCode)
        if not check:
            print("Register Incorrect")
            return
        check, memory = checkMemory(rm2, machineCode)
        if not check:
            print("Memory Out of Range")
            return

        # Get register values
        valuesReg = register.getData()
        machineCode.setReg(register.getCode())
        # Get Memory values
        # Memory Size is always 8
        valuesMem = memory.getData()
        # Set Reg code
        machineCode.setReg(register.getCode())

        if mode == 1:
            # mode = 1 = REG, Mem
            machineCode.setMode('0')  # Mode 0 Memory
            machineCode.setDBit('1')
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
            machineCode.setMode('0')  # Mode 0 memory
            machineCode.setDBit('0')  # D bit 0 = Reg to RM
            if register.size == 16:
                valuesReg = valuesReg[-8:]
            # Take AND
            for x in range(8):
                valuesMem[x] = valuesMem[x] | valuesReg[x]
            memory.inputList(valuesMem)
            return
    elif mode == 3:
        # mode = 3 = Reg, Reg
        check1, reg1 = checkRegister(rm1, machineCode)
        check2, reg2 = checkRegister(rm2, machineCode)
        if not check2 and check1:
            print("Registers Incorrect")
            return
        # Set Reg Codes
        machineCode.setReg(reg1.getCode())
        machineCode.setRM2(reg2.getCode())
        machineCode.setDBit('1')
        machineCode.setMode('1')  # Mode 11 RM is Register
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
        check, memory = checkMemory(rm2, machineCode)
        if not check:
            print("Memory Incorrect")
            return
        # Set RM
        machineCode.setMode('0')  # Mode 0 memory
        # Get mem value
        valueMem = memory.getData()
        # Pad zeros
        if len(binaryString) < 8:
            binaryString = '0' * (8 - len(binaryString)) + binaryString
        elif len(binaryString) > 8:
            binaryString = binaryString[-8:]
        # set imm
        machineCode.setImm(binaryString)
        # Take AND
        for x in range(8):
            valueMem[x] = valueMem[x] | int(binaryString[x])
        memory.inputList(valueMem)
        return
    elif mode == 5:
        # mode = 5 = reg, imm
        check, register = checkRegister(rm1, machineCode)
        if not check:
            print("Register Incorrect")
            return
        # Set Reg
        machineCode.setReg(register.getCode())
        # Get mem value
        valueReg = register.getData()
        # Pad zeros
        if len(binaryString) < register.size:
            binaryString = '0' * \
                (register.size - len(binaryString)) + binaryString
        elif len(binaryString) > register.size:
            binaryString = binaryString[-register.size:]
        # set imm
        machineCode.setImm(binaryString)
        # Take AND
        for x in range(register.size):
            valueReg[x] = valueReg[x] | int(binaryString[x])
        register.inputList(valueReg)
        return


# Opcode = 2
def XOR(mode, machineCode, rm1='', rm2='', binaryString=''):
    machineCode.setOpcode('0010')
    # rm1 will always be reg and rm2 may be reg or mem
    if mode == 1 or mode == 2:
        check, register = checkRegister(rm1, machineCode)
        if not check:
            print("Register Incorrect")
            return
        check, memory = checkMemory(rm2, machineCode)
        if not check:
            print("Memory Out of Range")
            return

        # Get register values
        valuesReg = register.getData()
        # Get Memory values
        # Memory Size is always 8
        valuesMem = memory.getData()
        # Set Reg code
        machineCode.setReg(register.getCode())

        if mode == 1:
            # mode = 1 = REG, Mem
            machineCode.setMode('0')  # Mode 0 Memory
            machineCode.setDBit('1')
            if register.size == 8:
                for x in range(8):
                    valuesReg[x] = valuesReg[x] ^ valuesMem[x]
                register.inputList(valuesReg)
                return
            else:
                # Register Size = 16
                for x in range(8):
                    valuesMem.insert(0, 0)
                for x in range(16):
                    valuesReg[x] = valuesReg[x] ^ valuesMem[x]
                register.inputList(valuesReg)
                return
        elif mode == 2:
            # mode = 2 = mem, Reg
            machineCode.setMode('0')  # Mode 0 memory
            machineCode.setDBit('0')  # D bit 0 = Reg to RM
            if register.size == 16:
                valuesReg = valuesReg[-8:]
            # Take AND
            for x in range(8):
                valuesMem[x] = valuesMem[x] ^ valuesReg[x]
            memory.inputList(valuesMem)
            return
    elif mode == 3:
        # mode = 3 = Reg, Reg
        check1, reg1 = checkRegister(rm1, machineCode)
        check2, reg2 = checkRegister(rm2, machineCode)
        if not check2 and check1:
            print("Registers Incorrect")
            return
        # Set Reg Codes
        machineCode.setReg(reg1.getCode())
        machineCode.setRM2(reg2.getCode())
        machineCode.setDBit('1')
        machineCode.setMode('1')  # Mode 11 RM is Register
        valuesReg1 = reg1.getData()
        valuesReg2 = reg2.getData()
        if reg1.size == 16 and reg2.size == 16:
            for x in range(16):
                valuesReg1[x] = valuesReg1[x] ^ valuesReg2[x]
        elif reg1.size == 8 and reg2.size == 8:
            for x in range(8):
                valuesReg1[x] = valuesReg1[x] ^ valuesReg2[x]
        elif reg1.size == 8 and reg2.size == 16:
            valuesReg2 = valuesReg2[-8:]
            for x in range(8):
                valuesReg1[x] = valuesReg1[x] ^ valuesReg2[x]
        elif reg1.size == 16 and reg2.size == 8:
            for x in range(8):
                valuesReg2.insert(0, 0)
            for x in range(16):
                valuesReg1[x] = valuesReg1[x] ^ valuesReg2[x]
        reg1.inputList(valuesReg1)
        return
    elif mode == 4:
        # mode = 4 = mem, imm
        check, memory = checkMemory(rm2, machineCode)
        if not check:
            print("Memory Incorrect")
            return
        # Set RM
        machineCode.setMode('0')  # Mode 0 memory

        # Get mem value
        valueMem = memory.getData()
        # Pad zeros
        if len(binaryString) < 8:
            binaryString = '0' * (8 - len(binaryString)) + binaryString
        elif len(binaryString) > 8:
            binaryString = binaryString[-8:]
        # set imm
        machineCode.setImm(binaryString)
        # Take AND
        for x in range(8):
            valueMem[x] = valueMem[x] ^ int(binaryString[x])
        memory.inputList(valueMem)
        return
    elif mode == 5:
        # mode = 5 = reg, imm
        check, register = checkRegister(rm1, machineCode)
        if not check:
            print("Register Incorrect")
            return
        # Set Reg
        machineCode.setReg(register.getCode())

        # Get mem value
        valueReg = register.getData()
        # Pad zeros
        if len(binaryString) < register.size:
            binaryString = '0' * \
                (register.size - len(binaryString)) + binaryString
        elif len(binaryString) > register.size:
            binaryString = binaryString[-register.size:]

        # set imm
        machineCode.setImm(binaryString)

        # Take AND
        for x in range(register.size):
            valueReg[x] = valueReg[x] ^ int(binaryString[x])
        register.inputList(valueReg)
        return


# Opcode = 5
def NOT(isMemory, machineCode, rm=''):
    machineCode.setOpcode('0101')
    if not isMemory:
        # Register
        check, register = checkRegister(rm, machineCode)
        if not check:
            print('Register Incorrect')
            return
        # Set Mode
        machineCode.setMode('1')  # Register Mode = 1
        # Set Reg
        machineCode.setReg(register.getCode())
        # Get reg values
        valuesReg = register.getData()

        # Take Not
        for x in range(register.size):
            if valuesReg[x] == 0:
                valuesReg[x] = 1
            else:
                valuesReg[x] = 0
        register.inputList(valuesReg)
    else:
        # Memory
        check, memory = checkMemory(rm, machineCode)
        if not check:
            print('Memory Incorrect')
            return
        # Set Mode
        machineCode.setMode('0')  # Memory Mode = 00
        # Get memory Values
        valuesMem = memory.getData()
        # Take Not
        for x in range(8):
            if valuesMem[x] == 0:
                valuesMem[x] = 1
            else:
                valuesMem[x] = 0
        memory.inputList(valuesMem)
