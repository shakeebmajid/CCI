#This is wrong

def setBit(num, i):
    mask = (1 << i)
    return (num | mask)

def clearBit(num, i):
    mask = ~(1 << i)
    return (num & mask)

def getBit(num, i):
    mask = (1 << i)
    return (num & mask) != 0


def nextLargest(num):
    count = 0
    for i in range(31):
        if getBit(num, i):
            if not getBit(num, i + 1):
                num = setBit(num, i + 1)
                num = clearBit(num, i)
                break

            else:
                print "count: ", count
                num = clearBit(num, i)
                num = setBit(num, count)
                count += 1

    return num

def nextSmallest(num):
    for i in range(31):
        if not getBit(num, i):
            if getBit(num, i + 1):
                num = setBit(num, i)
                num = clearBit(num, i + 1)
                break

    return num

def nextNumber(num):
    print bin(nextLargest(num))
    print bin(nextSmallest(num))

nextNumber(0b1011100)
