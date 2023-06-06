class Solution:
    def leaders(self, A, N):
        ans = []
        max = A[N-1]
        ans.append(max)
        for i in range(N-2, -1, -1):
            if max <= A[i]:
                max = A[i]
                ans.append(A[i])
        #ans = ans[:-1]
        return list(reversed(ans))

def main():
    T = int(input())
    while(T>0):
        n = int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ans = ob.leaders(a,n)
        for i in ans:
            print(i,end= " ")
        print()
        T -=1

if __name__ == "__main__":
    main()
