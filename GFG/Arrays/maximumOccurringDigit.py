class Solution:
    def maxoccourence (self, arr, n, k):
        
        #code here
        ans = 0
        maxi = 0
        
        for item in arr:
            count = 0
            for it in str(item):
                if k == int(it):
                    count += 1
            if count > maxi:
                maxi = count
                ans = item
                
            elif count == maxi and item < ans:
                ans = item
                
        return ans
