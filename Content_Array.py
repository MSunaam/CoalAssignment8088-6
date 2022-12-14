def compliment(value):
    listBin = list(value)
    length = len(listBin)
    first1 = False
    for char in range(length - 1, -1, -1):
        if listBin[char] == '0' and not first1:
            pass
        elif listBin[char] == '1' and not first1:
            first1 = True
        else:
            if listBin[char] == '1':
                listBin[char] = '0'
            else:
                listBin[char] = '1'

    return ''.join(map(str, listBin))


def convertToBinary(value, size=16, rM='Register'):
    if size != 16 and size != 8:
        print(f"{rM} can only be 16-bits or 8-bits")
        return

    binary = bin(value)
    str_bin = str(binary)
    negative = False

    if value < 0:
        # Value Negative need to store in 2's Complement Form
        str_bin = str_bin[3:]
        negative = True
    else:
        # Value not negative
        str_bin = str_bin[2:]

    str_bin = "0" * (size - len(str_bin)) + str_bin
    # filling the string with 0s

    if negative:
        # If negative take compliment
        str_bin = compliment(str_bin)

    if len(str_bin) > size:
        print(f"Size Mismatch: Register can hold {size}-bits only")
        return False
    else:
        return [int(x) for x in str_bin]


class Content_Array:
    # Note Lower is 8 to 15 and Higher is 0 to 7
    # This array will store 8-bits array
    def __init__(self):
        self.content = convertToBinary(0)
        # Initialize the array with 0s

    def getSign(self):
        # Return msb
        return self.content[0]

    def input(self, value):
        # 16-bits input into X
        if not convertToBinary(value):
            return
        # If size mismatch occurs, return and value not changes
        self.content = convertToBinary(value)

    def inputH(self, value):
        # 8-bits input into Higher(H)
        if not convertToBinary(value, 8):
            return
        # If size mismatch occurs, return and value not changes
        for x in range(8):
            self.content[x] = convertToBinary(value, 8)[x]
            # This will change only the first 8-bits

    def inputL(self, value):
        # 8-bits input into Lower(L)
        if not convertToBinary(value, 8):
            return
        # If size mismatch occurs, return and value not changes
        for x in range(8, 16):
            self.content[abs(x)] = convertToBinary(value, 8)[abs(x - 8)]
            # Content array needs to be accessed from 8 to 15 but convertToBinary needs to accessed from 0 to 7

    def swapHL(self):
        # For helping swap Higher and Lower for MOV commands
        # Save Higher in temp
        tempH = []
        for x in range(0, 8):
            tempH.append(self.content[x])
        # Put lower(8 to 15) into Higher(0 to 7)
        for x in range(8, 16):
            self.content[abs(x - 8)] = self.content[x]
        # Put tempH into lower(8 to 16)
        for x in range(8, 16):
            self.content[x] = tempH[abs(x - 8)]

    def getLow(self):
        # Get the lower part of the array
        return [self.content[x] for x in range(8, 16)]

    def getHigh(self):
        # Get the higher part of the array
        return [self.content[x] for x in range(8)]

    def getData(self):
        # Get the whole array
        return self.content

    def print(self):
        # Temp function to check Array (Testing)
        print(self.content)


class Content_Array_16(Content_Array):
    # This array is for creating 16-bit registers like CS and DS
    # In such registers it is not allowed to access 8-bits low or high
    def inputH(self, value):
        pass

    def inputL(self, value):
        pass

    def swapHL(self):
        pass

    def getLow(self):
        pass

    def getHigh(self):
        pass

    def SF(self, setFlag):
        if setFlag:
            self.content[15] = 1
        else:
            self.content[15] = 0

    def OF(self, setFlag):
        if setFlag:
            self.content[14] = 1
        else:
            self.content[14] = 0

    def ZF(self, setFlag):
        if setFlag:
            self.content[13] = 1
        else:
            self.content[13] = 0

    def CF(self, setFlag):
        if setFlag:
            self.content[12] = 1
        else:
            self.content[12] = 0
