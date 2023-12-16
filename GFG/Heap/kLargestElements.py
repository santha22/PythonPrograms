import heapq
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        maxHeap = []
        for it in li:
            heapq.heappush(maxHeap, -it)
            
        ans = []
        while k:
            val = heapq.heappop(maxHeap)
            ans.append(-val)
            k -= 1
            
        return ans
