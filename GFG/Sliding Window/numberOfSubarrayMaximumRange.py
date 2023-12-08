class Solution:
    def countSubarrays(self, a,n,l,r): 
        # Complete the function
        lessThanL = 0
        j = 0
        for i in range(n):
            if a[i] < l:
                lessThanL += (i - j + 1)
                
            else:
                j = i + 1
                
        j = 0
        lessThanEqualR = 0
        for i in range(n):
            if a[i] <= r:
                lessThanEqualR += (i - j + 1)
                
            else:
                j = i + 1
                
        return lessThanEqualR - lessThanL
