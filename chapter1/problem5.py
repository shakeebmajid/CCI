import unittest


def isOneAway(str1, str2):
    isEdited = False
    if abs(len(str1) - len(str2)) > 1:
        return False
    if len(str1) == len(str2):
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                if isEdited:
                    return False
                else:
                    isEdited = True
    return True

print("pale and ple are one edit away", isOneAway("pale","ple"))
print("pale and pals are one edit away", isOneAway("pale","pals"))
print("pale and bale are one edit away", isOneAway("pale","bale"))
