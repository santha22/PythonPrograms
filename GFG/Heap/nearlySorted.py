#User function Template for python3
import heapq
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        minHeap = []
        res = []
        
        for j in range(n):
            if len(minHeap) <= k:
                heapq.heappush(minHeap, a[j])
            else:
                val = heapq.heappop(minHeap)
                res.append(val)
                heapq.heappush(minHeap, a[j])
        
        while len(minHeap) > 0:
            val = heapq.heappop(minHeap)
            res.append(val)
        
        return res
            
        
