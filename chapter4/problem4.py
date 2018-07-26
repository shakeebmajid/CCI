def maxHeight(root):
    if root == None:
        return 0
    leftHeight = maxHeight(root.left) + 1
    rightHeight = maxHeight(root.right) + 1

    if leftHeight > rightHeight:
        return leftHeight
    
    else:
        return rightHeight

def checkBalanced(root):
    if root == None:
        return True

    if maxHeight(root.left) - maxHeight(root.right) > 1:
        return False

    return checkBalanced(root.left) and checkBalanced(root.right)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

b = Node(5)
b.left = Node(6)
b.right = Node(8)
b.left.left = Node(19)
b.left.left.right = Node(2)
b.right.left = Node(12)
#b.left.right = Node(-5)

print checkBalanced(b)
