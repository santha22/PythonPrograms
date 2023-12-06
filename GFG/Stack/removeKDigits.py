class Solution:

    def removeKdigits(self, s, k):
        # code here
        stack = []
        for c in s:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
                
            stack.append(c)
            
        stack = stack[: -k] if k > 0 else stack
        res = "".join(stack)
        
       
        
        return str(int(res)) if res else "0"
