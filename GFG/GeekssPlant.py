class Solution:
    def minimumBuckets(self,N, arr):
        gcd = arr[0]
        sum = arr[0]
        for i in range(1, N):
            gcd = self.computeGCD(gcd, arr[i])
            sum += arr[i]
        return int(sum / gcd)

    def computeGCD(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)


class IntArray:
    def __init__(self):
        pass
    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        N = int(input())
        arr = IntArray().Input()
        obj = Solution()
        res = obj.minimumBuckets(N,arr)
        print(res)




