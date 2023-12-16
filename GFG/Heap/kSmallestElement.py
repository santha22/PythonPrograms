import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        minHeap = []
        for it in arr:
            heapq.heappush(minHeap, it)
            
        i = 1
        while i < k:
            heapq.heappop(minHeap)
            i += 1
            
        return minHeap[0]
