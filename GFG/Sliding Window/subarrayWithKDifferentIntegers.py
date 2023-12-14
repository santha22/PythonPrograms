class Solution:
    def f(self, arr, k, n):
        i,j,total = 0,0,0
        mp = {}
        while j < n:
            mp[arr[j]] = 1 + mp.get(arr[j], 0)

            while len(mp) > k:
                mp[arr[i]] -= 1
                if mp[arr[i]] == 0:
                    mp.pop(arr[i])

                i += 1

            total += j - i + 1
            j += 1

        return total    
    
    def subarrayCount(self, arr, n, k):
        # Code here
        return self.f(arr, k, n) - self.f(arr, k - 1, n)
