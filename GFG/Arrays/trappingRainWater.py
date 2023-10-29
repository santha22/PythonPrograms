class Solution:
    def trappingWater(self, arr,n):
        #Code here
        leftMax = [0] * n
        rightMax = [0] * n
        ans = 0
        
        leftMax[0] = arr[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], arr[i])
            
        rightMax[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], arr[i])
                
        for i in range(n):
            ans += min(leftMax[i], rightMax[i]) - arr[i]
                
        
        return ans
