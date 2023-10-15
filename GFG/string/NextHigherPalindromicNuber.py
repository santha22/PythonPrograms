class Solution:
    def nextGreater(self, arr, n):
        temp = arr[:]
        k = n - 2
        while k >= 0 and temp[k] >= temp[k+1]:
            k -= 1
            
        if k < 0:
            temp = temp[::-1]
        
        else:
            for l in range(n-1, k, -1):
                if temp[l] > temp[k]:
                    break
                
            temp[l], temp[k] = temp[k], temp[l]
            temp[k+1:] = temp[k+1:][::-1]
            
        return temp
        
        
    
    def nextPalin(self, N):
        #code here
        n = len(N)
        
        if n <= 3:
            return -1
            
        s = list(N)
        
        m = n // 2
        if n % 2 != 0:
            mid = [s[m]]
            
        else:
            mid = [""]
           
        left = s[:m] 
        nextLeft = self.nextGreater(left, len(left))
        
        
        if int("".join(left)) >= int("".join(nextLeft)):
            return -1
        
        nextRight = nextLeft[::-1]
        return "".join(nextLeft + mid + nextRight)
       
