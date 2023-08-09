class Solution():
    def primeNumbers(self, n):
        l = set()
        if(n<=1):
            return []
        i = 2
        while(i*i<=n):
            while(n%i==0):
                l.add(i)
                n = n//i
            i += 1
        if(n>1):
            l.add(n)
        return sorted(list(l))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        ans = ob.primeNumbers(n)
        for i in ans:
            print(i,end=" ")
        print()