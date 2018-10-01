def recursiveMultiply(a, b):
    if a == 0 or b == 0:
        return 0

    if abs(a) > abs(b):
        temp = a
        a = b
        b = temp

    if a == 1:
        return b
    if a == -1:
        return -b

    if a < -1:
        if a % 2 == 1:
            return -(recursiveMultiply(-(a + 1), b) + b)
        else:
            return -(recursiveMultiply(- a / 2, b) << 1)

    if a % 2 == 1:
        return recursiveMultiply(a - 1, b ) + b
    else:
        return recursiveMultiply(a / 2, b) << 1


print "recursive multiply of 5 * 5: ", recursiveMultiply(5, 5)
print "recursive multiply of -60 * 13: ", recursiveMultiply(-60, 13)
print "recursive multiply of 13 * -67: ", recursiveMultiply(13, -67)
print "recursive multiply of -13 * 67: ", recursiveMultiply(-13, 67)
print "recursive multiply of -1 * 60: ", recursiveMultiply(-1, 60)
print "recursive multiply of 1 * -60: ", recursiveMultiply(1, -60)
print "recursive multiply of -1 * -60: ", recursiveMultiply(-1, -60)
print "recursive multiply of 0 * -60: ", recursiveMultiply(0, -60)

print """hi \n yo this is trips"""
print r'hi \n yo this is r'

if '':
    print "this was ran"

if -1:
    print "this -1 was ran"
    print "this too"

x = [1, 2]
y = x
y.append(3)
print x
