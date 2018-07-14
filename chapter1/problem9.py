def strRotation(s1, s2):
    doubleS2 = s2 + s2
    return  s1 in doubleS2

print("is 'erbottlewat' a rotation of 'waterbottle'?: ", strRotation('erbottlewat', 'waterbottle'))


