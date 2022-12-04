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