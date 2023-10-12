class Solution:
	def addBinary(self, a, b):
		# code here 
		x, y = 0, 0
		ans = ""
		carry = 0
		i = 0
		n = len(a)
		m = len(b)
		
		while i < n or i < m or carry != 0:
		    x, y = 0, 0
		    
		    if i < n and a[n - 1 - i] == "1":
		        x = 1
		        
		    if i < m and b[m - 1 - i] == "1":
		        y = 1
		       
		    cur = (x + y + carry) % 2
		    ans += str(cur)
		    carry = (x + y + carry) // 2
		    i += 1
		 
	    j = len(ans) - 1
	    
	    while j >= 0 and ans[j] == "0":
	        ans = ans[:-1]
	        j -= 1
	        
	    return ans[::-1]
	    
