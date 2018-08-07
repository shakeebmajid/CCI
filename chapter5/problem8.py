def setBit(num, i):
    mask = 1 << i
    return (num | mask)

def bitIndex(y, w, x):
    return y * w + x

def setByte(array, bitIndex):
    array[bitIndex / 8] = setBit(array[bitIndex / 8], 7 - bitIndex % 8)

def drawLine(screen, width, x1, x2, y):
    for i in range((x2 - x1) + 1):
        xn = x1 + i
        xnIndex = bitIndex(y, width, xn)
        setByte(screen, xnIndex)
    return screen
screen = [0b11111111, 0b11010001, 0b11100011, 0b11100011]

screen_with_line = drawLine(screen, 16, 10, 13, 0)

for byte in screen_with_line:
    print bin(byte)
