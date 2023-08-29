import math

def setBits(xorValue):
    count = 0
    while(xorValue):
   s     if(xorValue % 2):
            count += 1
        xorValue = int(xorValue / 2)

    return count

def minFlips(n, k):
    # number of bits in n
    size = int(math.log2(n) + 1)

    # find largest number of same size with k set bits
    max = pow(2, k) - 1
    max = max << (size - k)

    # count bit difference to find required flipping
    xorValue = (n ^ max)
    return setBits(xorValue)


n = 14
k = 2
print("min Flips = ", minFlips(n, k))
