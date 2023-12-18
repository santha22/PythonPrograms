
class Solution:
    def searchInsertK(self, arr, n, k):
        # code here
        l,h = 0,n - 1
        ans = n
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] == k:
                return mid
                
            elif arr[mid] < k:
                l = mid + 1
                
            else:
                ans = mid
                h = mid - 1
                
                
        return ans
