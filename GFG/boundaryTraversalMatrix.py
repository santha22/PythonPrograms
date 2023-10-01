class Solution:

    def BoundaryTraversal(self, matrix, n, m):
        # code here
        left = 0
        right = m - 1
        up = 0
        down = n - 1
        ans = []

        if n == 1:
            for i in range(m):
                ans.append(matrix[0][i])

            return ans

        if m == 1:
            for j in range(n):
                ans.append(matrix[j][0])

            return ans

        for i in range(right + 1):
            ans.append(matrix[left][i])

        for j in range(up + 1, down + 1):
            ans.append(matrix[j][right])

        for k in range(right - 1, left - 1, -1):
            ans.append(matrix[down][k])

        for l in range(down - 1, up, -1):
            ans.append(matrix[l][left])

        return ans
