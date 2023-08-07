class Solution:
    def Reverse(self,arr,start,end):
        while(start<end):
            arr[start], arr[end] = arr[end],arr[start]
            start += 1
            end -= 1

    def leftRotate(self,arr,k,n):
        if(n==0):
            return
        k = k % n
        self.Reverse(arr,0,k-1)
        self.Reverse(arr,k,n-1)
        self.Reverse(arr,0,n-1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        k = int(input())
        arr = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(arr,k,n)
        print(*arr)
