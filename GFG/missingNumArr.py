class Solution:
    def missingNumber(self, array, n):
        originalSum = int(n*(n+1)/2)
        sum=0
        for i in array:
            sum = sum + i
        num = originalSum - sum
        return num


t = int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution.missingNumber(a,n)
    print(s)
