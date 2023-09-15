import heapq


class Solution:
    # Function to return k largest elements from an array.
    def kLargest(self, arr, k):
        # code here
        ans = []
        for item in arr:
            heapq.heappush(ans, -item)

        res = []
        for i in range(k):
            if ans:
                item = heapq.heappop(ans)
                res.append(-item)

        return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = list(map(int, input().split()))
        n = a[0]
        k = a[1]
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.kLargest(arr, k)
        for i in ans:
            print(i, end=" ")
        print()