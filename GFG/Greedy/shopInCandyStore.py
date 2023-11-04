class Solution:

    def candyStore(self, candies, n, k):
        # code here
        mini, maxi = 0, 0
        candies.sort()
        
        val = n // (k + 1)
        if n % (k + 1) != 0:
            val += 1
            
        for i in range(n):
            if i < val:
                mini += candies[i]
                
        candies.reverse()
        
        for i in range(n):
            if i < val:
                maxi += candies[i]
                
        return [mini, maxi]
