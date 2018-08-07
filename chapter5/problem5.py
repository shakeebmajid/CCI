
def getBit(num, i):
    mask = (1 << i)
    return (mask & num) != 0

def numFlips(A, B):
    count = 0
    numOfOpposites = (A ^ B)
    for i in range(32):
        if getBit(numOfOpposites, i):
            count += 1
    return count

print numFlips(0b11101, 0b01111)
