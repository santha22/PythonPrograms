import heapq


class Solution:
    def topK(self, nums, k):
        # Code here

        count = {}
        ans = []

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        max_heap = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (-freq, -num))

        for i in range(k):
            if max_heap:
                freq, num = heapq.heappop(max_heap)
                ans.append(-num)

        return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = list(map(int, input().split()))
        n = a[0]
        nums = a[1:]
        k = int(input())
        ob = Solution()
        ans = ob.topK(nums, k)
        for i in ans:
            print(i, end=" ")
        print()