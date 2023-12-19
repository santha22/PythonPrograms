class Solution:
      
    def firstOccurrence(self, arr, n, x):
        first = -1
        l,h = 0, n - 1
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] == x:
                first = mid
                h = mid - 1
    
            elif arr[mid] < x:
                l = mid + 1
    
            else:
                h = mid - 1
    
        return first

    def lastOccurrence(self, arr, n, x):
        l,h = 0,n - 1
        last = -1
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] == x:
                last = mid
                l = mid + 1
    
            elif arr[mid] < x:
                l = mid + 1
    
            else:
                h = mid - 1
    
        return last


    
	def count(self,arr, n, x):
		# code here
		first,last = self.firstOccurrence(arr, n, x), self.lastOccurrence(arr, n, x)
    
        if first == -1:
            return 0
    
        return last - first + 1
    
        return next - last + 1
