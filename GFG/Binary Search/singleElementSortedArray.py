class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        l,h = 0, len(arr) - 1
        if len(arr) == 1:
            return arr[0]
    
        m = (l + h) // 2
        while l <= m:
            if arr[l] != arr[l + 1] and l + 1 < len(arr):
                return arr[l]
    
            l += 2
    
        m = m + 1
        while m <= h:
            if arr[h] != arr[h - 1] and h - 1 >= 0:
                return arr[h]
    
            h -= 2
