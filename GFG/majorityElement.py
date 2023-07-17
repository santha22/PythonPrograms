#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here 
        dict = {}
        for i in range(N):
            if A[i] in dict:
                dict[A[i]] += 1
            else:
                dict[A[i]] = 1
         
        for i in dict:
            if dict[i] > N//2:
                return i
        return -1
            
        
