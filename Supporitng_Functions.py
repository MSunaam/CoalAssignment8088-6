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
