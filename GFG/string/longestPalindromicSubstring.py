class Solution:


    def longestPalindrome(self, s):
        # code here
        n = len(s)
        dp = [[0] * (n) for i in range(n)]
        ans = ""
        maxLen = 0
        for diff in range(n):
            i = 0
            j = i + diff
            while j < n:
                if i == j:
                    dp[i][j] = 1
                        
                elif diff == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 0
                    
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                        
                        
                if dp[i][j]:
                    if  j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        ans = s[i: j + 1]
                        
                i += 1
                
                j += 1
                        
        return ans
