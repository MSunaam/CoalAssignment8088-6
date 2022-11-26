def convertToBinary(value, size=16):
    # Default argument 16 for whole register
    if size == 16 or size == 8:
        binary = bin(value)
        str_bin = str(binary)
        str_bin = str_bin[2:]
        if len(str_bin) > size:
            print(f"Size Mismatch: Register can hold {size}-bits only")
        else:
            str_bin = "0" * (size - len(str_bin)) + str_bin
            # filling the string with 0s
            return [int(x) for x in str_bin]
