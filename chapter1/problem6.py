def compress (s):
    currentChar = s[0]
    currentCount = 1
    compressedStr = "" + s[0]
    for char in s[1:]:
        if char == currentChar:
            currentCount += 1
        else:
            compressedStr += str(currentCount) + char
            currentChar = char
            currentCount = 1
    compressedStr += str(currentCount)
    if len(compressedStr) >= len(s):
        return s
    else: 
        return compressedStr

print("aabcccccaaa compressed is: ", compress("aabcccccaaa"))
