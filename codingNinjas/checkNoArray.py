def checkNumber(arr,x):
    n = len(arr)
    if n == 0:          #base case
        return False
    elif arr[0] == x:   #condition
        return True 
    smallOutput = arr[1:]                #induction hypothesis  this is taking too much space hence we can replace
    output = checkNumber(smallOutput,x)   
    return output


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:   
    print('false')
