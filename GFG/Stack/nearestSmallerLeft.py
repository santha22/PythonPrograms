
class Solution:
    def leftSmaller(self, n, a):
        # code here 
        stack = []
        ans = [-1] * n
        for i in range(n):
            if len(stack) == 0:
                ans[i] = -1
                
            elif stack and stack[-1] < a[i]:
                ans[i] = stack[-1]
                
            elif stack and stack[-1] >= a[i]:
                while stack and stack[-1] >= a[i]:
                    stack.pop() 
                    
                if len(stack) == 0:
                    ans[i] = -1
                    
                else:
                    ans[i] = stack[-1]
                    
            stack.append(a[i])
            
        return ans
