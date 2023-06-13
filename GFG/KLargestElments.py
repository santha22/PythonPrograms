class Solution:
    def kLargest(self, arr, n, k):
        if n==0:
            return ""
        else:
            a = sorted(arr,reverse=True)
            l = []
            for i in range(k):
                l.append(a[i])
            return l


if __name__ == "__main__":
    t = int(input())
    while t>0:
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n,k)
        for x in ans:
            print(x, end=" ")
        print()
        t -= 1