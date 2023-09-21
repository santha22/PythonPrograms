class Solution:
    def canPair(self, nums, k):
        mp = {}
        for i in range(len(nums)):
            rem = nums[i] % k
            mp[rem] = 1 + mp.get(rem, 0)

        if mp.get(0, 0) % 2 != 0:
            return False

        if k % 2 == 0:
            if mp.get(k // 2, 0) % 2 != 0:
                return False

        for i in range(1, (k // 2) + 1):
            if mp.get(i, 0) != mp.get(k - i, 0):
                return False

        return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        n, k = s[0], s[1]
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if ans:
            print("True")
        else:
            print("False")