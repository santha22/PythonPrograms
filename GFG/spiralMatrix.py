class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        # code here
        left, top = 0, 0
        bottom, right = r - 1, c - 1
        res = []

        while (top <= bottom and left <= right):
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            if (top <= bottom):
                for k in range(right, left - 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1

            if (left <= right):
                for l in range(bottom, top - 1, -1):
                    res.append(matrix[l][left])
                left += 1

        return res

        left, top = 0, 0
        right, bottom = r - 1, c - 1
        ans = []

        while (top <= bottom and left <= right):
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if (top <= bottom):
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if (left <= right):
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        r,c = map(int, input().split())
        values = list(map(int, input().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)

        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()
