class Solution:
    def findKRotation(self,arr,  n):
        # code here
        l,h = 0,len(arr) - 1
        mini = float("inf")
        while l <= h:
            mid = (l + h) // 2
            if arr[l] <= arr[mid]:
                if arr[l] < mini:
                    mini = arr[l]
                    ind = l
    
                l = mid + 1
    
            else:
                l = l + 1
                h = h - 1
    
        return ind
