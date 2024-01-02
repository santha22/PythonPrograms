class Solution:

    def lowerBound(self, arr, n, x):
        low = 0
        high = n - 1
        ans = n
    
        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] >= x:
                ans = mid
                # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right
        return ans
        
	def rowWithMax1s(self,arr, n, m):
		# code here
		cnt_max = 0
        index = -1
    
        # traverse the rows:
        for i in range(n):
            # get the number of 1's:
            cnt_ones = m - self.lowerBound(arr[i], m, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
                
        return index
