import heapq
class Solution:
    def distinctIds(self,arr : list, n : int, m : int):
        # Complete this function
        mp = {} 
        for i in arr:
            mp[i] = 1 + mp.get(i, 0)
        
        minHeap = []
        for i in mp:
            heapq.heappush(minHeap, [mp[i], i])
        
        while m and minHeap:
            cnt, val = heapq.heappop(minHeap)
            m -= 1
            cnt -= 1
            if cnt != 0:
                heapq.heappush(minHeap, [cnt, val]) 
        
        return len(minHeap)
    
