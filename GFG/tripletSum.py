class Solution:

    # Function to find if there exists a triplet in the
    # array A[] which sums up to X.
    def find3Numbers(self, A, n, x):
        # Your Code Here
        A.sort()

        for i in range(n):
            if (i > 0 and A[i] == A[i - 1]):
                continue

            j = i + 1
            k = n - 1

            while (j < k):

                summ = A[i] + A[j] + A[k]

                if (summ < x):
                    j += 1
                elif (summ > x):
                    k -= 1
                else:
                    return True

        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = list(map(int,input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        if(ob.find3Numbers(arr, n, x)):
            print(1)
        else:
            print(0)