import heapq
class Solution:
    def nearlySorted(self, a, n, k):
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

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().split()))
        a = list(map(int, input().split()))
        ob = Solution()
        print(*ob.nearlySorted(a, n, k))