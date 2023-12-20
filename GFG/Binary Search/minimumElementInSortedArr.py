class Solution:
    def findMin(self, arr, n):
        #complete the function here
        l,h = 0, len(arr) - 1
        mini = float("inf")
        while l <= h:
            mid = (l + h) // 2
            if arr[l] <= arr[mid]:
                mini = min(mini, arr[l])
                l = mid + 1

            else:
                l = l + 1
                h = h - 1
    
        return mini
