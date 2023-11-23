class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,s):
        # code here 
        ans = s.split(".")
        n = len(ans)
        ans1 = []
        for i in range(n - 1, 0, -1):
            
            ans1.append(ans[i])
            
        ans1.append(ans[0])
            
        return ".".join(ans1)
