class Solution:
    def check(self,A,B,N):
        A.sort()
        B.sort()
        for i in range(0,N):
            if (A[i] != B[i]):
                return False
        return True
                

        



t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().strip().split()]
    b=[int(x) for x in input().strip().split()]

    ob = Solution()
    if ob.check(a,b,n):
        print(1)
    else:
        print(0)
