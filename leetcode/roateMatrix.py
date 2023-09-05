def roate(matrix):

    n = len(matrix)
    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        left = 0
        right = len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    return matrix


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        matrix = []
        for i in range(0,n*n, n):
            matrix.append(arr[i:i+n])
        roate(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
