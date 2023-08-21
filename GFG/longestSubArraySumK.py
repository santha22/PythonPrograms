class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        csum = 0
        maxLen = 0
        prefixDict = {}
        j = 0
        while (j < n):

            csum += arr[j]

            if (csum == k):
                maxLen = j + 1

            rem = csum - k
            if (rem in prefixDict):
                maxLen = max(maxLen, j - prefixDict[rem])

            if (csum not in prefixDict):
                prefixDict[csum] = j
            j += 1

        return maxLen
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = print(ob.lenOfLongSubarr(arr, n, k))
