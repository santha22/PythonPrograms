import heapq
class Solution:
    def isStraightHand(self, n, groupSize, hand):
        # Code here
        if len(hand) % groupSize:
            return False
            
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
            
        minheap = list(count.keys())
        heapq.heapify(minheap)
        
        while minheap:
            first = minheap[0]
            
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                    
                count[i] -= 1
                if count[i] == 0:
                    if i != minheap[0]:
                        return False
                        
                    heapq.heappop(minheap)
                    
        return True
