def zeroMatrix(matrix):
    zeroCols = {}
    zeroRows = {}
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if matrix[m][n] == 0:
                print("this was his at: ", " m: ", m, " n: ", n)
                if n not in zeroCols and m not in zeroRows:
                    for m0 in range(len(matrix)):
                        matrix[m0][n] = 0
                    for n0 in range(len(matrix[m])):
                        print("m: ", m, "n0: ", n0)
                        matrix[m][n0] = 0
                    zeroCols[n] = True
                    zeroRows[m] = True
    return matrix

matrix = [[1, 0, 2], [1, 3, 4], [5, 6, 0]]
print("zero matrix is: ", zeroMatrix(matrix))

