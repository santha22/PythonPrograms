class Solution:
	def matSearch(self,mat, n, m, x):
		# Complete this function
		
        for i in range(n):
            l, h = 0, m - 1
            while l <= h:
                mid = (l + h) // 2
    
                if mat[i][mid] == x:
                    return 1
    
                elif mat[i][mid] > x:
                    h = mid - 1
    
                else:
                    l = mid + 1
    
        return 0
