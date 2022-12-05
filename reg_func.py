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
        return

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
    # Get Opcode
    machineCode.setOpcode('1101')
    # Set mode
    machineCode.setMode('1')
    # Check register
    check, register = checkRegister(reg, machineCode)
    if not check:
        print('Invalid Register')
        return
    # Get register Code
    machineCode.setReg(register.getCode())
    # Get immediate data
    # Set imm
    data = bin(imm if imm > 0 else imm + (1 << 8))[2:]
    data = data.zfill(8)
    machineCode.setImm(data)
    # Transfer to reg
    register.input(imm)
    return