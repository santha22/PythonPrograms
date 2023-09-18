import heapq
import math

class Solution:
    def kClosest(self, points, k: int):
        minHeap = []
        for i in range(len(points)):
            val1 = abs(points[i][0]) ** 2
            val2 = abs(points[i][1]) ** 2
            val = math.sqrt(val1 + val2)
            heapq.heappush(minHeap, [val, points[i]])

        ans = []
        while k:
            val, point = heapq.heappop(minHeap)
            ans.append(point)
            k -= 1

        return ans

