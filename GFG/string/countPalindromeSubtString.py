class Solution:

    def countpalin(self, s, left, right):
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
            
        return count
        
    def CountPS(self, s, n):
        # code here
        res = 0
        for i in range(n):
            even = self.countpalin(s, i, i + 1)
            odd = self.countpalin(s, i, i)
            res += even + odd 
            
        return res - n
