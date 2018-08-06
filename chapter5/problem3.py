
def getBit(num, index):
    return ((1 << index) & num) != 0

def countLeftOnes(zeroIndex, num):
    count = 0
    index = zeroIndex + 1
    while index != 32:
        if getBit(num, index):
            count += 1
        else:
            break
        index += 1
    return count

def countRightOnes(zeroIndex, num):
    count = 0
    index = zeroIndex - 1
    while index != -1:
        if getBit(num, index):
            count += 1
        else:
            break
        index -= 1
    return count

def flipBitToWin(num):
    max = 0
    ones = 0
    for i in range(32):
        if not getBit(num, i):
            count = countLeftOnes(i, num) + countRightOnes(i, num) + 1
            ones = 0
            if count > max:
                max = count
        else:
            ones += 1
            if ones > max:
                max = ones
    return max

print "flip: ", flipBitToWin(0b1111)
