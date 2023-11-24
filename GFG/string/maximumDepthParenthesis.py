    def maxDepth(self, s):
        # Code here 
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                
            elif s[i] == ')':
                count = max(count, len(stack))
                    
                    
                stack.pop() 
                
        return count
