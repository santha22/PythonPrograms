def firstIndexB(a, x, si):
    l = len(a)
    if si == l:
        return -1
    if a[si] == x:
        return si
    smallerListOutput = firstIndexB(a, x, si+1)
    return smallerListOutput

n = int(input())
a = list(int(i) for i in input().strip().split(' '))
x = int(input())
si = 0
print(firstIndexB(a,x,si))
