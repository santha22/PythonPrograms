class Solution:
    def update(self, a, n, updates, k):
        # Your code goes here
        for i in range(k):
            j = updates[i]
            a[j - 1] += 1

        for i in range(1, n):
            a[i] += a[i - 1]

if __name__ == "__main__":
    t = int(input())

    while(t>0):
        s = [int(x) for x in input().strip().split()]
        n,k = s[0], s[1]
        a= [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.update(a,n,updates,k)
        print(*a)
        t-=1