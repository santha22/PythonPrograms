import heapq


class Solution:
    def frequency(self, arr, n):
        hashMap = {}
        for i in range(n):
            hashMap[arr[i]] = 1 + hashMap.get(arr[i], 0)

        res = []

        maxHeap = []
        for it in hashMap:
            heapq.heappush(maxHeap, [-hashMap[it], it])

        while maxHeap:
            freq, num = heapq.heappop(maxHeap)
            for i in range(abs(freq)):
                res.append(num)

        return res


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(*ob.frequency(arr, n))
