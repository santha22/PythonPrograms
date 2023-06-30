
def kadaneAlgo(a):
    N=len(a)
    curSum = 0
        msf=arr[0]
        for i in range(N):
            curSum+=arr[i]
            if msf < curSum:
                msf = curSum
            if curSum < 0:
                curSum = 0
            
        return msf


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadaneAlgo(A))
