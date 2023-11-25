class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    ans = [[1], [1, 1]]
	    for row in range(2, n + 1):
	        temp = [1]
	        for col in range(1, row):
	            val = (ans[row - 1][col - 1] + ans[row - 1][col]) % (10**9 + 7)
	            temp.append(val)
	            
	        temp.append(1)
	        ans.append(temp)
	        
	    return ans[n - 1]
