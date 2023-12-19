
class Solution:
    def search(self, arr : list, l : int, h : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        while l <= h:
            mid = (l + h) // 2
            
            if arr[mid] == key:
                return mid
                
            if arr[l] <= arr[mid]:
                if arr[l] <= key and key <= arr[mid]:
                    h = mid - 1
                
                else:
                    l = mid + 1
                
            else:
                if arr[mid] <= key and key <= arr[h]:
                    l = mid + 1
                    
                else:
                    h = mid - 1
                    
                    
        return -1
