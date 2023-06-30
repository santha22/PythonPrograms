
def kadaneAlgo(a):
    sum = 0
    maxA = a[0]
    for i in range(len(a)):
        sum = sum + a[i]
        [i]
        maxA = max(maxA,sum)
        if sum < 0:
            sum = 0
    return maxA


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadaneAlgo(A))