import unittest

def setZeros(N, M, i, j):
    maskHelper = (2 ** ((j - i) + 1)) - 1
    shiftedMaskHelper = maskHelper << i
    # print("shifted helper: ", bin(shiftedMaskHelper))
    shiftedM = M << i
    # print("shifted m: ", bin(shiftedM))
    mask = ~(shiftedM ^ shiftedMaskHelper)
    # print "output: ", bin(N & mask)
    return N & mask

def setOnes(N, M, i, j):
    mask = M << i
    return N | mask

def insertion(N, M, i, j):
    N = setZeros(N, M, i, j)
    N = setOnes(N, M, i, j)
    return N

print "Insertion result: ", insertion(0b10000000000, 0b10011, 2, 6)

class TestInsertion(unittest.TestCase):
    def setUp(self):
        nCases = [0b1011001, 0b100000, 0b001001, 0b0, 0b1]
        mCases = [0b101, 0b00, 0b11, 0b1, 0b0]
        iCases = [2, 3, 3, 0, 0]
        jCases = [4, 4, 4, 0, 0]


if __name__ == '__main__':
    unittest.main()
