def lastIndex(a,x):
    l = len(a)
    if l == 0:
        return -1
    smallerList = a[1:]
    smallerListOutput = lastIndex(smallerList,x)

    if smallerListOutput != -1:
        return smallerListOutput + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1

n = int(input())
a = list(int(i) for i in input().strip().split())
x = int(input())
print(lastIndex(a,x))


        
    
