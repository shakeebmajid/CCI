import unittest

def isPermPal(str):
    matches = 0
    chars = len(str)
    d = {}
    for char in str:
        if char in d:
            matches += 1
        else:
            if char == " ":
                chars -= 1
            else:
                d[char] = True
    if chars / 2 == matches:
        return True
    else:
        return False

print("'tcoa_tca' is a permutation of a palindrome: ", isPermPal("tcoa tca"))

