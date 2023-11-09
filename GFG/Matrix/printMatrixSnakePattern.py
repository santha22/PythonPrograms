class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
        
           
        ans = [] 
        n = len(matrix) 
        flag = 0
        for row in range(n): 
            if flag == 0: 
                col = 0
                while col < n: 
                   ans.append(matrix[row][col]) 
                   col += 1 
                flag = 1
            
            else: 
                col = n - 1 
                while col > -1: 
                    ans.append(matrix[row][col])
                    col -= 1
                
                flag = 0
            
        return ans
