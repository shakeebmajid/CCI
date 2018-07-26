class Node: 
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

def minTree(array):
    if len(array) == 0:
        return None

    mid = len(array) / 2
    root = Node(array[mid])
    
    if len(array) == 1:
        print("root is: ", root.data)
        return root

    root.left = minTree(array[:mid])
    root.right = minTree(array[mid + 1:])

    print("root is: ", root.data)
    return root

minTree([-1, 0, 2, 6, 8, 9])
