class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        mp = {}
        for i in range(n):
            mp[arr[i]] = 1 + mp.get(arr[i], 0)
        
        for i in range(n):
            if i + 1 in mp and i+1 <= n:
                arr[i] = mp[i+1] 
             
            else: 
                arr[i] = 0
         
        return arr
