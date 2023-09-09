def rotate(matrix):
    # code here

    n = len(matrix)
    for row in matrix:
        row.reverse()

    for i in range(n - 1):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        matrix = []
        for i in range(0, n*n, n):
            matrix.append(arr[i:i+n])

        rotate(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=' ')
            print()