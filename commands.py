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
