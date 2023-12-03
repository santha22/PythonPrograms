class Solution:
    def nextLargerElement(self,arr,n):
        #code here 
        stack  = []
        ans = [-1] * n
        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                ans[i] = -1
                
            elif stack and stack[-1] > arr[i]:
                ans[i] = stack[-1]
                
            elif stack and stack[-1] <= arr[i]:
                while stack and stack[-1] <= arr[i]:
                    stack.pop()
                    
                if len(stack) == 0:
                    ans[i] = -1
                    
                else:
                    ans[i] = stack[-1]
            
            stack.append(arr[i])
            
        return ans
