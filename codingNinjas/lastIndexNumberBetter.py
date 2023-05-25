def lastIndexB(a, x, si):
    l = len(a)
    if si == l:
        return -1
    smallerListOutput = lastIndexB(a, x , si+1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if a[si] == x:
            return si
        else:
            return -1

n = int(input())
a = list(int(i) for i in input().strip().split())
x = int(input())
si = 0
print(lastIndexB(a,x,si))
