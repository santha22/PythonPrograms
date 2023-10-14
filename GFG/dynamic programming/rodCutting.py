
class Solution:
    
    def cutRod(self, price, n):
        #code here
        vector<int> prev(n+1, 0), cur(n+1, 0));
        cur = [0] * (n + 1)
    
        for N in range(n + 1):
            prev[N] = N * price[0]
    
        for ind in range(1, n):
            for N in range(n + 1):
                notTake = 0 + prev[N]
                take = float("-inf")
                rodLength = ind + 1
    
                if rodLength <= N:
                    take = price[ind] + cur[N - rodLength]
    
                cur[N] = max(take, notTake)
    
            prev = cur[:]
    
        return prev[n]
