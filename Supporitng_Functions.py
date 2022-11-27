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
