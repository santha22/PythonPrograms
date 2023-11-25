class Solution:
    def removeOuter(self, s):
        # Code here
        stack = []
        ans = ""
        for i in range(len(s)):
            if s[i] == '(':
                if len(stack) > 0:
                    ans += s[i]
                    
                stack.append(s[i])
                
            else:
                stack.pop()
                if len(stack) > 0:
                    ans += s[i]
                    
        return ans
