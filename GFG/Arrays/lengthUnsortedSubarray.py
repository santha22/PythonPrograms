class Solution:

	def printUnsorted(self,arr, n):
		# code here
		s = 0
		for s in range(n - 1):
		    if arr[s] > arr[s + 1]:
		        break
		    
		if s == n - 1:
		    return [0, n - 1]
		    
		for e in range(n - 1, 0, -1):
		    if arr[e] < arr[e - 1]:
		        break
		    
		maxi = arr[s]
		mini = arr[s]
		
		for i in range(s + 1, e + 1):
		    if arr[i] > maxi:
		        maxi = arr[i]
		        
		    if arr[i] < mini:
		        mini = arr[i]
		        
		for i in range(s):
		    if arr[i] > mini:
		        s = i
		        break
		    
		 
		    
		for i in range(n - 1, e, -1):
            if arr[i] < maxi:
                e = i
                break
		    
		return [s, e]
              
