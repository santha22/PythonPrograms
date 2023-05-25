def sumArray(arr):
    l=0
    #pass
    for i in arr:
        l= l+int(i)
    return l

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))

