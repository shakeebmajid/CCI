import unittest

def binaryToString(val):
    place = 0.5
    binRep = 0b0
    i = 0
    while i != 32 and val != 0:
        binRep <<= 1
        if place <= val:
            binRep += 1
            val -= place
        place /= 2
        i += 1
    return binRep

print bin(binaryToString(0.625))
