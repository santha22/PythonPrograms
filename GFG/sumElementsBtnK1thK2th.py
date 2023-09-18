import heapq
class Solution:
    def sumBetweenTwoKth(self, a, n, k1, k2):
        minHeap = []
        for i in range(n):
            heapq.heappush(minHeap, a[i])

        val = k2 - k1 - 1
        ans = 0
        while k1 > 0:
            heapq.heappop(minHeap)
            k1 -= 1

        while val > 0:
            ans += heapq.heappop(minHeap)
            val -= 1

        return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = list(map(int, input().split()))
        k1, k2 = s[0], s[1]
        ob = Solution()
        print(ob.sumBetweenTwoKth(a, n, k1, k2))
