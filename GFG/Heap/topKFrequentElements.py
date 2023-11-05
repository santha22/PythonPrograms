import heapq
class Solution:
	def topK(self, nums, k):
		#Code here
        
        mp = {}
        li = []
        
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
            
        maxHeap = []
        for val, freq in mp.items():
            heapq.heappush(maxHeap, [-freq, -val])

        for i in range(k):
            if maxHeap:
                freq, val = heapq.heappop(maxHeap)
                li.append(-val)
                
        return li
