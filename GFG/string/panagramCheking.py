class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        alpha = [0] * 26
        
        if len(s) < 26:
            return 0
        
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                alpha[ord(i) - ord("A")] += 1
                
            elif ord(i) >= 97 and ord(i) <= 122:
                alpha[ord(i) - ord("a")] += 1
                
        for i in range(26):
            if alpha[i] == 0:
                return 0
                
        
        return 1
