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
