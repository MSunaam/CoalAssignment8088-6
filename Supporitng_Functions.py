import re
from Register_Instances import *


def stringToList(string):
    listW = re.findall(r'\w+', string)
    return listW


def checkRegisters(registers):
    if registers[0] == registers[1]:
        print("Same Register Referenced Twice")
        return False
    correctRegisters = False
    if len(registers) > 1:
        if registers[0] in Reg and registers[1] in Reg:
            correctRegisters = True
        elif registers[0] in subRegLow or registers[0] in subRegHigh and registers[1] in subRegHigh or registers[
            1] in subRegLow:
            correctRegisters = True
        else:
            correctRegisters = False
    else:
        if registers in Reg or registers in subRegLow or registers in subRegHigh:
            correctRegisters = True
        else:
            correctRegisters = False
    return correctRegisters


def checkOperands(string):
    listWords = stringToList(string)

    if len(listWords) < 3:
        print("Operand Error: One or more operands are missing")
        return

    # Check if immediate data passed
    if listWords[2].isnumeric():
        value = listWords[2]

    # Check if memory used
    matches = re.findall(r'\[(.*?)\]', string)

    if len(matches) > 1:
        # This will be an error as we need at least one register
        print("Operand Error: At least one register is required")
    elif len(matches) == 0:
        # Both are Registers
        # Pass listWords except the first index
        if not checkRegisters(listWords[1:]):
            print("Operand Error: Incorrect Registers")
            return
    else:
        # One register one memory


