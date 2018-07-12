def isUnique(str):
    map = {}
    for char in str:
        if map[char]:
            return False
        else:
            map[char] = True
    return True

print("banana is unique evaluates to: ", isUnique("banana"))
