class Solution:

    # Function to merge the arrays.
    def merge(self, arr1, arr2, n, m):
        # code here
        left = n - 1
        right = 0
        while (left >= 0 and right < m):
            if (arr1[left] > arr2[right]):
                arr1[left], arr2[right] = arr2[right], arr1[left]
                left -= 1
                right += 1

            else:
                break

        arr1.sort()
        arr2.sort()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        ob = Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1, end=" ")
        print(*arr2)
