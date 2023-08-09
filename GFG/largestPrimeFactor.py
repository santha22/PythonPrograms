class Solution:
    def largestPrimeFactor(self,n):
        l = []
        if(n<=1):
            return n
        i = 2
        while(i*i<=n):
            while(n%i==0):
                l.append(i)
                n = n//i
            i+=1
        if(n>1):
            l.append(n)
        return max(l)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.largestPrimeFactor(n))