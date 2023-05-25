def firstIndex(a, x):
    l = len(a)
    if l == 0:
        return -1
    if a[0] == x:
        return 0
    smallerList = a[1:]
    smallerListOutput = firstIndex(smallerList, x)

    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1
"""
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(firstIndex(arr,x))"""


from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
