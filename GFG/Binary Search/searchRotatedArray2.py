class Solution:
    def Search(self, n, arr, k):
        # code here
        l,h = 0,n - 1
        while l <= h:
            mid = (l + h) // 2
    
            if arr[mid] == k:
                return 1
    
            if arr[l] == arr[mid] and arr[mid] == arr[h]:
                l += 1
                h -= 1
                continue
            
            if arr[l] <= arr[mid]:
                if arr[l] <= k and k <= arr[mid]:
                    h = mid - 1
    
                else:
                    l = mid + 1
    
    
            else:
                if arr[mid] <= k and k <= arr[h]:
                    l = mid + 1
    
                else:
                    h = mid - 1
        
        return 0
