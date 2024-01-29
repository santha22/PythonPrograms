
class Solution:
    
    def maximumPoints(self, points, n):
        # Code here
        dp = [[0 for i in range(4)] for j in range(n)]

        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    
        for day in range(1, n):
            for last in range(4):
                maxi = 0
    
                for task in range(3):
                    if task != last:
                        score = points[day][task] + dp[day - 1][task]
                        maxi = max(maxi, score)
    
                dp[day][last] = maxi
    
        return dp[n - 1][3]
                    
                
                
        
