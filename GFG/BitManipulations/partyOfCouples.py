class Solution:
    def getOddOccurrence(self, arr, n):
        # code here
        xor = 0
        for i in range(n):
            xor = xor ^ arr[i]

        return xor

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.getOddOccurrence(arr, n))
