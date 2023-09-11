class Solution:
    def sumK(self, arr, n, k):

        mpp = {0: 1}
        pre_sum = 0
        cnt = 0

        for i in range(len(arr)):
            pre_sum += arr[i]
            remove = pre_sum - k
            cnt += mpp.get(remove, 0)
            mpp[pre_sum] = mpp.get(pre_sum, 0) + 1

        return cnt

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        print(ob.sumK(arr, n, k))