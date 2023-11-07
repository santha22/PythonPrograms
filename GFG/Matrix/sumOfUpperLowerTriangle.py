class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        ans, ans1 = 0, 0
        for row in range(n):
            for col in range(n):
                if row <= col:
                    ans += matrix[row][col]
                
                if row >= col:
                    ans1 += matrix[row][col]
            
            
                
        return [ans, ans1]
