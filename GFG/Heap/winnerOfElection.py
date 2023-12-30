import heapq
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        maxi = -1
        
        val = arr[0][0]
        
        mp = {}
        
        for i in arr:
            mp[i] = 1 + mp.get(i, 0)
            
        
        maxHeap = []   
        for it in mp:
            heapq.heappush(maxHeap, [-mp[it], it])
                
                
        val, s = heapq.heappop(maxHeap) 
        return [s, -val]
