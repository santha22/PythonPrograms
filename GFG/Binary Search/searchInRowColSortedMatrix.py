class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
    	# code here 
        
        row, col = 0, m - 1
        
        while row < n and col >= 0:
        
            
            if matrix[row][col] == target:
                return 1
                
            elif matrix[row][col] < target:
                row += 1
                
            else:
                col -= 1
                
        return 0
