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
