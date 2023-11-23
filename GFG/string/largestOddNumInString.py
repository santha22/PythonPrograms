class Solution:
    def maxOdd(self, s):
        val = ""
        ans = ""
        for it in s:
            val += it
            if int(val) % 2 != 0:
                ans = val
                
        return ans
