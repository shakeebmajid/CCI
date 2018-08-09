def robotInAGrid(i, j, grid):
    r = len(grid)
    c = len(grid[0])

    if i == r or j == c or grid[i][j] == 1:
        return None

    if i == (r - 1) and j == (c - 1):
        return [(r - 1, c - 1)]

    down = robotInAGrid(i + 1, j, grid)
    if down:
        down = [(i, j)] + down
        return down

    right = robotInAGrid(i, j + 1, grid)
    if right:
        right = [(i, j)] + right
        return right
    return None

def robotInAGridMain(grid):
    return robotInAGrid(0, 0, grid)


grid = [[0, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0]]
print robotInAGridMain(grid)
