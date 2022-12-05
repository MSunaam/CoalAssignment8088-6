from MachineCode import MachineCode
from Supporitng_Functions import stringToList, isMemory, checkMemory
from Register_Instances import *
from Memory_Instances import *
from commands import *

machineCodes = MachineCode()


def stringToFunction(string, machineCode):
    string = string.lower()
    listOperands = stringToList(string)
    memory = isMemory(string)

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
            return
    else:
        # No memory Operand
        memory = None

    # Check first operand to determine function
    if listOperands[0] == 'mov':
        # Check if move valid
        if len(listOperands) != 3:
            print('Error Invalid Command')
            return False
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
                    movRegReg(machineCode, listOperands[1], listOperands[2])
                else:
                    # Second Operand is imm
                    moveRegImm(machineCode, listOperands[1], listOperands[2])
            else:
                # First operand is not a register
                print("Invalid Operands")
                return False
        else:
            # Memory is used
            # Check first operand
            if listOperands[1] in SubReg.keys() or listOperands[1] in Reg.keys():
                # Second Operand must be Memory
                moveRegMem(machineCode, listOperands[1], listOperands[2].upper())
            elif listOperands[2] in SubReg.keys() or listOperands[2] in Reg.keys():
                # Check if second operand is register
                # Then first operand is memory
                moveMemReg(machineCode, listOperands[2].upper(), listOperands[1])
            else:
                # Immediate Data
                movMemImm(machineCode, listOperands[1].upper(), listOperands[2])
    elif listOperands[0] == 'inc':
        # Check operands
        if len(listOperands) > 2:
            print("Error, Invalid Operands")
            return False
        if memory is not None:
            # Increment Register
            inc(machineCode, listOperands[1], False)
        else:
            # Increment Memory
            inc(machineCode, listOperands[1], True)
    elif listOperands[0] == 'dec':
        # Check operands
        if len(listOperands) > 2:
            print("Error, Invalid Operands")
            return False
        if memory is not None:
            # Increment Register
            dec(machineCode, listOperands[1], False)
        else:
            # Increment Memory
            dec(machineCode, listOperands[1].upper(), True)
    elif listOperands[0] == 'ror':
        # Check if memory or register
        if memory is None:
            # register
            ror(machineCode, listOperands[1], int(listOperands[2]), False)
        else:
            # memory
            ror(machineCode, listOperands[1][1].upper(), int(listOperands[2]), True)
    elif listOperands[0] == 'rol':
        # Check if memory or register
        if memory is None:
            # Register
            rol(machineCode, listOperands[1], int(listOperands[2]), False)
        else:
            # memory
            rol(machineCode, listOperands[1][1].upper(), int(listOperands[2]), False)


AX.input(5)
BX.input(2)
mem['F'].input(2)

string = input("A")

stringToFunction(string, machineCodes)

AX.printContent()
