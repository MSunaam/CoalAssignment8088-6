# Opcode = 14
def movMemImm(machineCode, mem, imm):
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
        value = returnDecimal(register)
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