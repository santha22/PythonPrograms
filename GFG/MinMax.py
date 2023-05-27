def getMinMax(a,n):
    min=a[0]
    max=a[0]
    for i in range(n):
        if(min>a[i]):
            min=a[i]
        if(max<a[i]):
            max=a[i]

    return min, max

T=int(input())
while(T>0):
    n=int(input())
    a=[int(x) for x in input().strip().split()]
    product=getMinMax(a,n)
    print(product[0],end=" ")
    print(product[1])
    T-=1
