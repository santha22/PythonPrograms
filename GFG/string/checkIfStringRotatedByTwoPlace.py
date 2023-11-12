
class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def swap(self, l, h, arr):
        while l < h:
            arr[l], arr[h] = arr[h], arr[l]
            l += 1
            h -= 1
            
        return arr
        
    def leftRotation(self, arr):
        n = len(arr)
        arr[:] = self.swap(0, 1, arr)
        arr[:] = self.swap(2, n - 1, arr)
        arr[:] = self.swap(0, n - 1, arr)
        
        return "".join(arr)
        
    def rightRotation(self, arr):
        n = len(arr)
        arr[:] = self.swap(0, n - 3, arr)
        arr[:] = self.swap(n - 2, n - 1, arr)
        arr[:] = self.swap(0, n - 1, arr)
        
        return "".join(arr)
    
    def isRotated(self, str1, str2):
        if self.leftRotation(list(str1)) == str2 or self.rightRotation(list(str1)) == str2:
            return 1
            
        return 0
