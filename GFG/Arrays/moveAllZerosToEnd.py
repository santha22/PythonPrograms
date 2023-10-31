class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	i,j = 0,0
    	flag = 0
    	while j < n:
    	    
    	        
    	    if arr[j] == 0 and flag == 0 and arr[i] != 0:
    	        i = j 
    	        flag = 1
    	        
    	    if arr[i] == 0 and arr[j] != 0:
    	        arr[i], arr[j] = arr[j], arr[i]
    	        flag = 0
    	        i += 1
    	        
    	    j += 1
