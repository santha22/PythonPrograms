class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        arr.sort()
        x = arr[0]
        y = arr[-1]
        ans=""
        for i in range(min(len(x),len(y))):
            if x[i]!=y[i]:
                if len(ans)==0:
                    return -1
                return ans
            ans+=x[i]
            
        return ans
        
       
