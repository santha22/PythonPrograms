class Solution:
	def findRank(self, S):
		#Code here 
		n = len(S)
		if n <= 1:
		    return 1
		    
		arr = [0]*26
		for i in range(n):
		    arr[ord(S[i]) - ord("a")] += 1
		    
		fact = [0]*n
		fact[0] = 1
		fact[1] = 1
		for i in range(2, n):
		    fact[i] = fact[i - 1] * i
		    
		res = 1
		for i in range(n):
		    count = 0
		    for j in range(ord(S[i]) - ord("a")):
		        count += arr[j]
		    arr[ord(S[i]) - ord("a")] -= 1
		    res += (count * fact[n - 1 - i])
		    
		return res
