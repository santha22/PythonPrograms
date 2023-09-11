class Solution:
    def findTwo(self, arr, n):
        sn = int((n*(n+1))/2)
        s2n = int(((n*(n+1)*(2*n+1)))/6)

        s,s2 = 0, 0
        for i in range(n):
            s += arr[i]
            s2 += arr[i]*arr[i]

        val1 = s - sn   # x - y
        val2 = s2 - s2n   # x*2 - y*2
        val2 = int(val2 / val1)    # x + y
        x = int((val1 + val2)/2)
        y = x - val1

        return [x, y]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob  = Solution()
        res = ob.findTwo(arr, n)
        for i in res:
            print(i, end=" ")

