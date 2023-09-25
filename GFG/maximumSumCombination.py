import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort()
        B.sort()

        maxHeap = []
        for i in range(N):
            heapq.heappush(maxHeap, [-A[i] - B[N - 1], N - 1])

        res = []
        while maxHeap and K > 0:
            curSum, ind = heapq.heappop(maxHeap)

            res.append(-curSum)

            if ind - 1 >= 0:
                heapq.heappush(maxHeap, [curSum + B[ind] - B[ind - 1], ind - 1])

            K -= 1

        return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        N, K = s[0], s[1]
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        print(*ob.maxCombinations(N, K, A, B))



