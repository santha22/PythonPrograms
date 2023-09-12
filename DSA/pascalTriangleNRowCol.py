def rowCol(row, column):

    res = 1
    for col in range(column):
        res = res * (row - col)
        res = int(res/(col+1))

    return res

row = 3
column = 2
print(rowCol(row, column))