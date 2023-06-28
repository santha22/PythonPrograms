class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Your code here
        sum = 0
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return -1
        sumArr = []
        for i in range(N):
            sum = sum + A[i]
            sumArr.append(sum)
        print(sumArr)
        total = sumArr[-1]
        print(total)
        for i in range(1, N - 1):
            sumLeft = sumArr[i] - A[i]
            sumRight = total - sumArr[i]
            if sumLeft == sumRight:
                return i + 1

        return -1

import math

def main():
    T = int(input())
    while(T>0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.equilibriumPoint(A,N))
        T -= 1

if __name__ == "__main__":
    main()


# 42
# 4 42 27 16 28 3 4 5 9 3 31 5 5 29 10 18 35 35 33 19 41 23 8 32 9 5 8 18 35 13 6 7 6 10 11 13 37 2 25 7 28 43