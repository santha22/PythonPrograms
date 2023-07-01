class Solution:
    def setBits(self, N):
        binary = bin(N)[2:]
        count=0
        for i in binary:
            if i=="1":
                count+=1
        return count

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.setBits(n)
        print(ans)