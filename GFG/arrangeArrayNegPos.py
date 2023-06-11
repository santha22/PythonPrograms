class Solution:
    def Rearrange(self, n, arr):
        self.mergeSort(arr,0,n-1)

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l+r)//2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l,mid,r)

    def merge(self, arr, l, mid, r):
        i = l
        while(i <= mid and arr[i]<0):
            i+=1
        j = mid+1
        while(j <= r and arr[j]<0):
            j+=1
        self.reverse(arr,i,mid)
        self.reverse(arr,mid+1,j-1)
        self.reverse(arr,i,j-1)


    def reverse(self, arr, l, r):
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1

if __name__ == '__main__':
    t = Solution()
    arr = [-3, 1, 0, -2]
    t.Rearrange(len(arr), arr)
    print(arr)



