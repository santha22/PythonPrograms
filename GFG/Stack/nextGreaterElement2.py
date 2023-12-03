class Solution:
    def nextGreaterElement(self, n, arr):
        # Code here
        ans = [-1] * n
        stack = []
        for i in range(2*n - 1, -1, -1):
            if len(stack) == 0:
                ans[i % n] = -1
                
            elif stack and stack[-1] > arr[i % n]:
                ans[i % n] = stack[-1]
                
            elif stack and stack[-1] <= arr[i % n]:
                while stack and stack[-1] <= arr[i % n]:
                    stack.pop() 
                    
                if len(stack) == 0:
                    ans[i % n] = -1
                    
                else:
                    ans[i % n] = stack[-1]
                    
            stack.append(arr[i % n]) 
            
        return ans
