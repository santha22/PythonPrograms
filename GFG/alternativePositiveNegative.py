class Solution:
    def rearrange(self,arr,n):
        a=[]
        b=[]
        for i in range(n):
            if(arr[i]>=0):
                a.append(arr[i])
            else:
                b.append(arr[i])
        i,j,k=0,0,0
        while(i<len(a) and j<len(b)):
            arr[k]=a[i]
            k+=1
            i+=1
            arr[k]=b[j]
            k+=1
            j+=1
        while(i<len(a)):
            arr[k]=a[i]
            k+=1
            i+=1
        while(j<len(b)):
            arr[k]=b[j]
            k+=1
            j+=1
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        ob = Solution()
        ob.rearrange(arr,n)
        for x in arr:
            print(x,end=" ")
        print()