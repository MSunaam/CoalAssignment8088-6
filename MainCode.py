from MachineCode import MachineCode
from Supporitng_Functions import stringToList, isMemory, checkMemory
from Register_Instances import *
from Memory_Instances import *
from commands import *

machineCodes = MachineCode()


def stringToFunction(string, machineCode):
    errorMsg = ''
    string = string.lower()
    listOperands = stringToList(string)
    memory = isMemory(string)

    if len(listOperands) == 1 or len(listOperands) > 3:
        errorMsg += 'Invalid Number of Operands'
        return errorMsg

    if len(memory) > 1:
        # At max each instruction can have 1 memory operand
        return False
    elif len(memory) == 1:
        # One memory operand
        memory = memory[0].upper()
        check, memory = checkMemory(memory, machineCode)
        if not check:
            # Memory is not in range
            print("Memory is not in range")
            errorMsg += "Memory is not in range"
            return errorMsg
    else:
        # No memory Operand
        memory = None

    # Check first operand to determine function
    if listOperands[0] == 'mov':
        # Check if move valid
        if len(listOperands) != 3:
            print('Error Invalid Command')
            errorMsg += 'Error Invalid Command'
            return errorMsg
        # Check which move
        # Check if memory exists
        if memory is None:
            # Both are reg or regs imm
            # First operand must be a register
            # Check first operand if it is register
            if listOperands[1] in SubReg.keys() or listOperands[1] in Reg.keys():
                # Check second operand
                if listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                    # Second operand is a Register
                    errorMsg = movRegReg(
                        machineCode, listOperands[1], listOperands[2])
                    if errorMsg is not None:
                        return errorMsg
                else:
                    # Second Operand is imm
                    errorMsg = moveRegImm(
                        machineCode, listOperands[1], listOperands[2])
                    # Check if register immediate is valid
                    if errorMsg is not None:
                        return errorMsg
            else:
                # First operand is not a register
                print("Invalid Operands")
                errorMsg += "Invalid Operands"
                return errorMsg
        else:
            # Memory is used
            # Check first operand
            if listOperands[1] in SubReg.keys() or listOperands[1] in Reg.keys():
                # Second Operand must be Memory
                moveRegMem(
                    machineCode, listOperands[1], listOperands[2][1].upper())
            elif listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Check if second operand is register
                # Then first operand is memory
                moveMemReg(
                    machineCode, listOperands[2], listOperands[1][1].upper())
            else:
                # Immediate Data
                movMemImm(
                    machineCode, listOperands[1][1].upper(), listOperands[2])
    elif listOperands[0] == 'inc':
        # Check operands
        if len(listOperands) > 2:
            print("Error, Invalid Operands")
            errorMsg += 'Error, Invalid Operands'
            return errorMsg
        if memory is None:
            # Increment Register
            inc(machineCode, listOperands[1], False)
        else:
            # Increment Memory
            inc(machineCode, listOperands[1], True)
    elif listOperands[0] == 'dec':
        # Check operands
        if len(listOperands) > 2:
            print("Error, Invalid Operands")
            errorMsg += "Error, Invalid Operands"
            return errorMsg
        if memory is None:
            # Increment Register
            dec(machineCode, listOperands[1], False)
        else:
            # Increment Memory
            dec(machineCode, listOperands[1][1].upper(), True)
    elif listOperands[0] == 'ror':
        # Check if memory or register
        if memory is None:
            # register
            ror(machineCode, listOperands[1], int(listOperands[2]), False)
        else:
            # memory
            ror(machineCode, listOperands[1][1].upper(), int(
                listOperands[2]), True)
    elif listOperands[0] == 'rol':
        # Check if memory or register
        if memory is None:
            # Register
            rol(machineCode, listOperands[1], int(listOperands[2]), False)
        else:
            # memory
            rol(machineCode, listOperands[1][1].upper(), int(
                listOperands[2]), False)
    elif listOperands[0] == 'shl':
        # Check if memory or register
        if memory is None:
            # Register
            shl(machineCode, listOperands[1], int(listOperands[2]), False)
        else:
            shl(machineCode, listOperands[1][1].upper(), int(
                listOperands[2]), True)
    elif listOperands[0] == 'shr':

        # Check if memory or register
        if memory is None:
            # Register
            shr(machineCode, listOperands[1], int(listOperands[2]), False)
        else:
            shr(machineCode, listOperands[1][1].upper(), int(
                listOperands[2]), True)
    elif listOperands[0] == 'and':
        # Check if memory
        if memory is None:
            # Check if reg reg or reg imm
            if listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Reg Reg
                AND(3, machineCode, listOperands[1], listOperands[2])
            else:
                # Reg imm
                AND(5, machineCode, listOperands[1], '', listOperands[2])
        else:
            # Memory used
            # check if reg mem
            if listOperands[1] in SubReg.keys() or listOperands[1] in Reg.keys():
                # Reg Mem
                AND(1, machineCode,
                    listOperands[1], listOperands[2][1].upper())
            elif listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Mem Reg
                AND(2, machineCode,
                    listOperands[2], listOperands[1][1].upper())
            else:
                # Mem Imm
                AND(4, machineCode, '',
                    listOperands[1][1].upper(), listOperands[2])
    elif listOperands[0] == 'xor':
        # Check if memory
        if memory is None:
            # Check if reg reg or reg imm
            if listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Reg Reg
                XOR(3, machineCode, listOperands[1], listOperands[2])
            else:
                # Reg imm
                XOR(5, machineCode, listOperands[1], '', listOperands[2])
        else:
            # Memory used
            # check if reg mem
            if listOperands[1] in SubReg.keys() or listOperands[1] in Reg.keys():
                # Reg Mem
                XOR(1, machineCode,
                    listOperands[1], listOperands[2][1].upper())
            elif listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Mem Reg
                XOR(2, machineCode,
                    listOperands[2], listOperands[1][1].upper())
            else:
                # Mem Imm
                XOR(4, machineCode, '',
                    listOperands[1][1].upper(), listOperands[2])
    elif listOperands[0] == 'or':
        # Check if memory
        if memory is None:
            # Check if reg reg or reg imm
            if listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Reg Reg
                OR(3, machineCode, listOperands[1], listOperands[2])
            else:
                # Reg imm
                OR(5, machineCode, listOperands[1], '', listOperands[2])
        else:
            # Memory used
            # check if reg mem
            if listOperands[1] in SubReg.keys() or listOperands[1] in Reg.keys():
                # Reg Mem
                OR(1, machineCode, listOperands[1], listOperands[2][1].upper())
            elif listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Mem Reg
                OR(2, machineCode, listOperands[2], listOperands[1][1].upper())
            else:
                # Mem Imm
                OR(4, machineCode, '',
                   listOperands[1][1].upper(), listOperands[2])
    elif listOperands[0] == 'not':
        # Check if memory or register
        if len(listOperands) > 2:
            print('Invalid Command')
            errorMsg += 'Invalid Command'
            return errorMsg
        if memory is None:
            # Register
            NOT(False, machineCode, listOperands[1])
        else:
            # Memory
            NOT(True, machineCode, listOperands[1][1].upper())
