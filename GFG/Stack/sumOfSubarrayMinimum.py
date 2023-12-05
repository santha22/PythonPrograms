class Solution:
    def sumSubarrayMins(self, n, arr):
        # Code here
        s1 = []
        s2 = []
        nextSmaller = [0] * n
        preSmaller = [0] * n
        for i in range(n):
            nextSmaller[i] = n - i - 1
            preSmaller[i] = i
            
        for i in range(n):
            while s1 and arr[s1[-1]] > arr[i]:
                nextSmaller[s1[-1]] = i - s1[-1] - 1
                s1.pop() 
                
            s1.append(i) 
            
        for i in range(n - 1, -1, -1):
            while s2 and arr[s2[-1]] >= arr[i]:
                preSmaller[s2[-1]] = s2[-1] - i - 1
                s2.pop() 
                
            s2.append(i)
            
        ans = 0
        mod = 1e9 + 7
        for i in range(n):
            ans += (arr[i] * (preSmaller[i] + 1) * (nextSmaller[i] + 1))
            
        return ans
