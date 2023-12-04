class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        ans = [1] * n
        
        stack  = []
        for i in range(n):
            if len(stack) == 0:
                ans[i] = -1
                
                
            elif stack and stack[-1][0] > a[i]:
                ans[i] = stack[-1][1]
                
            elif stack and stack[-1][0] <= a[i]:
                    
                while stack and stack[-1][0] <= a[i]:
                    stack.pop()  
                    
                if len(stack) == 0:
                    ans[i] = -1
                    
                else:
                    ans[i] = stack[-1][1]
                    
            stack.append([a[i], i])
            
        for i in range(n):
            ans[i] = i - ans[i]
