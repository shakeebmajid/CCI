import unittest

def isUnique(str):
    map = {}
    for char in str:
        if char in map:
            return False
        else:
            map[char] = True
    return True

def isUniqueWithoutSpace(str):
    if str[0]==str[-1]:
        return False
    sortStr = ''.join(sorted(str))
    lastChar = sortStr[0]
    for char in sortStr[1:]:
        if char == lastChar:
            return False
        else:
            lastChar = char
    return True

def checkPerm(str1, str2):
    if len(str1) != len(str2):
        return False
    sortStr1 = sorted(str1)
    sortStr2 = sorted(str2)
    for char1, char2 in zip(sortStr1, sortStr2):
       if char1 != char2:
            return False
    return True
print(checkPerm("dog", "god"))

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.nonUnique = ['banana', 'cherry', 'apple']
        self.unique = ['mango', 'grape', 'pear']

    def test_unique_true(self):

        for str in self.unique:
            actual = isUnique(str)
            self.assertTrue(actual)

    def test_unique_false(self):

        for str in self.nonUnique:
            actual = isUnique(str)
            self.assertFalse(actual)

    def test_unique_no_space_true(self):

        for str in self.unique:
            actual = isUniqueWithoutSpace(str)
            self.assertTrue(actual)

    def test_unique_no_space_false(self):

        for str in self.nonUnique:
            actual = isUniqueWithoutSpace(str)
            self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
