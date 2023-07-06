class Solution:
    
    def swap(self, a, b, arr):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        
    def quickSort(self,arr,low,high):
        
        if low < high:
            pi = self.partition(arr,low, high)
            
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
        
    
    def partition(self,arr,low,high):
        
        pivot_index = low
        pivot = arr[pivot_index]
        
        while low < high:
            while low < len(arr) and arr[low] <= pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
                
            if low < high:
                self.swap(low, high , arr)
        
        self.swap(pivot_index, high, arr)
        
        return high
    

if __name__  == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().quickSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i], end=" ")
        print()