class Solution:
    def merge(self, arr, l, m, r):
        i = l
        j = m + 1
        ans = []
        
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                ans.append(arr[i])
                i += 1
                
            else:
                ans.append(arr[j])
                j += 1
                
        while i <= m:
            ans.append(arr[i])
            i += 1
            
        while j <= r:
            ans.append(arr[j])
            j += 1
            
        for k in range(l, r + 1):
            arr[k] = ans[k - l]
            
    def countpair(self, l, mid, h, arr):
        right = mid + 1
        count = 0
        for i in range(l, mid + 1):
            while right <= h and arr[i] > 2 * arr[right]:
                right += 1
                
            count += (right - (mid + 1))
            
        return count
                
        
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            count = 0
            
            count += self.mergeSort(arr, l, mid)
            count += self.mergeSort(arr, mid + 1, r)
            count += self.countpair(l, mid, r, arr)
            self.merge(arr, l, mid, r)
            
            return count
            
        return 0
        
    def countRevPairs(self, n, arr):
        # Code here
        return self.mergeSort(arr, 0, n - 1)
        
        
