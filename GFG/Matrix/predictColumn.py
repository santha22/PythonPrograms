class Solution:
    def columnWithMaxZeros(self,arr,n):
        # code here 
        maxi = 0
        val, ans = -1, -1
        for col in range(n):
            count = 0
            for row in range(n):
                if arr[row][col] == 0:
                    count +=1
                    val = col
                    
            if count > maxi:
                maxi = count
                ans = val
                
        if ans == -1:
            return ans
            
        
        return ans
