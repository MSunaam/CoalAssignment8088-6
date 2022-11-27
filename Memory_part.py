def hex_to_decimal(value): #uses value as string passed as hex
    if value[0] == '-':
        value = value[1:]
        h=hex_to_decimal(value)
        h= str(h)
        h="-"+h
        return h
    elif len(value) < 3:
        d = int(value, base=16)
        return d
    else:
        print("Incorrect Value..")
# print(hex_to_decimal("-F"))

def flip(value):
    return "1" if value=="0" else "0"


def checknegative(value):
    if value[0]=="-":
        return True
    else:
        return False

def binaryToDecimal(n):
    return int(n,2)




# print(complemented_value("10"))
# print(bin(10))
print(bin(6))
complemented_value("6")



