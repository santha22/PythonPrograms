
class Solution:

    def lookandsay(self, n):
        # code here
        if n == 1:
            return "1"
        
        if n == 2:
            return "11"
            
        s = "11"
        for i in range(3, n + 1):
            s += "$"
            cnt = 1
            l = len(s)
            temp = ""
            
            for j in range(1, l):
                if s[j] != s[j - 1]:
                    temp += str(cnt)
                    temp += s[j - 1]
                    
                    cnt = 1
                    
                else:
                    cnt += 1
                
            s = temp
        
        return s
