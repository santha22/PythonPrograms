import heapq


class Solution:
    def kthLargest(self, k, arr, n):

        minHeap = []

        for i in range(k):
            heapq.heappush(minHeap, arr[i])

        ans = [-1] * (k - 1)
        ans.append(minHeap[0])

        for i in range(k, n):

            if minHeap[0] > arr[i]:
                ans.append(minHeap[0])


            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, arr[i])
                ans.append(minHeap[0])

        return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        k,n = s[0],s[1]
        arr = list(map(int, input().split()))
        ob = Solution()
        print(*ob.kthLargest(k,arr,n))
