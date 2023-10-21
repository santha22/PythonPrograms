class Solution:
    def sumOfDivisors(self, n):
    	#code here 
    	curSum = 0
    	for i in range(1, n + 1):
    	    curSum += (n // i) * i
    	    
    	return curSum
