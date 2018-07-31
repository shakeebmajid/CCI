class node:
    def __init__(self, data):
        self.data = data
        self.adjacentNodes = []
        self.visited = False

def clean(n1, n2):
    n1.visited = False
    queue = Queue()
    queue.put(n1)
    while not queue.empty():
        currentNode = queue.get()
        for adjacentNode in currentNode.adjacentNodes:
            if adjacentNode.visited:
                adjacentNode.visited = False
                queue.put(adjacentNode)

def bfs(n1, n2):
    n1.visited = True
    queue = Queue()
    queue.put(n1)
    while not queue.empty():
        currentNode = queue.get()
        for adjacentNode in currentNode.adjacentNodes:
            if adjacentNode is n2:
                return True
            if not adjacentNode.visited:
                queue.put(adjacentNode)
                adjacentNode.visited = True
    return False

def isRoute(n1, n2):
    if bfs(n1, n2):
        return True

    clean(n1, n2)
    
    if bfs(n2, n1):
        return True

    return False
