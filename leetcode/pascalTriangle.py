class Solution(object):
    def generateRow(self, row):
        ans = 1
        ansRow = [1]
        for col in range(1, row):
            ans = int((ans * (row - col)) / col)
            ansRow.append(ans)

        return ansRow

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(1, numRows + 1):
            ans.append(self.generateRow(i))

        return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        res = ob.generate(n)
        for i in res:
            print(i, end=" ")
        print()