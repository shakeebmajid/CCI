class BITree:
    def __init__(self, arr):
        self.fenwick_tree = [0] * (len(arr) + 1)
        self.arr = arr
        for i in range(1, len(self.fenwick_tree)):
            last_set_bit = i & -i
            sum = 0
            for j in range(i - last_set_bit, i):
                sum += arr[j]

            self.fenwick_tree[i] = sum

    def update(self, i, val):
        added = val - self.arr[i]
        index = i + 1
        while index < len(self.fenwick_tree):
            self.fenwick_tree[index] += added
            index += index & -index

    def range(self, i):
        index = i + 1
        sum = 0
        while index > 0:
            sum += self.fenwick_tree[index]
            index -= index & -index
        return sum

    def sum(self, begin, end):
        return self.range(end) - self.range(begin - 1)
arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
print(arr)
bitree = BITree(arr)
print("fenwick tree: ", bitree.fenwick_tree)

print("range(6)", bitree.range(6))
print("range(0)", bitree.range(0))
print("range(1)", bitree.range(1))
print("range(2)", bitree.range(2))
print("range(3)", bitree.range(3))
print("range(4)", bitree.range(4))
print("range(5)", bitree.range(5))
print("range(6)", bitree.range(6))
print("range(7)", bitree.range(7))
print("range(8)", bitree.range(8))
print("range(9)", bitree.range(9))
print("range(10)", bitree.range(10))

print("sum(0, 10)", bitree.sum(0, 10))
print("sum(1, 10)", bitree.sum(1, 10))
print("sum(2, 10)", bitree.sum(2, 10))
print("sum(3, 10)", bitree.sum(3, 10))
print("sum(4, 10)", bitree.sum(4, 10))
print("sum(5, 10)", bitree.sum(5, 10))
print("sum(6, 10)", bitree.sum(6, 10))
print("sum(7, 10)", bitree.sum(7, 10))
print("sum(8, 10)", bitree.sum(8, 10))
print("sum(9, 10)", bitree.sum(9, 10))
print("sum(10)", bitree.sum(10, 10))
