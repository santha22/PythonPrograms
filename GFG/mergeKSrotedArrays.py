import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        minHeap = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                heapq.heappush(minHeap, arr[i][j])

        ans = []

        while minHeap:
            ans.append(heapq.heappop(minHeap))

        return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        numbers = [[0 for i in range(n)] for j in range(n)]
        line = input().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j] = int(line[i*n+j])

        ob = Solution()
        merged_list = ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i, end=" ")
