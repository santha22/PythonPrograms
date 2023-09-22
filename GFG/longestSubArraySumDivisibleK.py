class Solution:
    def longSubarrWthSumDivByK(self, arr, n, k):
        # Complete the function
        mp = {0: -1}
        summ = 0
        length = 0

        for i in range(n):
            summ += arr[i]

            rem = summ % k

            if rem < 0:
                rem += k

            if rem in mp:
                length = max(length, i - mp[rem])

            if rem not in mp:
                mp[rem] = i

        return length

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        n, k = s[0], s[1]
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.longSubarrWthSumDivByK(arr, n, k))