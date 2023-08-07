def f(l,r):
    if(l>=r):
        return
    arr[l],arr[r] = arr[r],arr[l]
    f(l+1,r-1)

arr = list(map(int, input().split()))
f(0,len(arr)-1)
print(arr)