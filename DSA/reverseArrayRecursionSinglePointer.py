def f(i):
    if(i>=len(arr)//2):
        return
    arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    f(i+1)

arr = list(map(int,input().split()))
f(0)
print(arr)