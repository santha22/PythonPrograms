class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,s):
        # code here 
        i, j = 0, 0
        word = ""
        res = ""
        n = len(s)
        while i < n:
            while i < n and s[i] == ".":
                i += 1
                
            if i >= n:
                break 
            
            j = i + 1
            while j < n and s[j] != ".":
                j += 1
                
            word = s[i: j]
            if len(res) == 0:
                res = word 
                
            else:
                res = word + "." + res 
                
            i = j + 1
            
        return res
