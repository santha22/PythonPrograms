class Solution:
    def arrange(self, arr, n):
        l = []
        for i in range(n):
            a = arr[arr[i]]
            l.insert(i,a)
        arr = l
        """for i in range(n):
            arr[i] = l[i]"""
        return arr

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        obj.arrange(arr,n)
        for i in arr:
            print(i, end=" ")
        print()
