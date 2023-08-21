class Solution:
    def count(self, arr, n, x):
        first_occurence = 0
        left = 0
        right = n - 1
        while (left <= right):
            mid = (right + left) // 2

            if (arr[mid] == x):
                first_occurence = mid
                right = mid - 1

            elif (arr[mid] < x):
                left = mid + 1

            else:
                right = mid - 1

        if (first_occurence == -1):
            return 0

        # finding second occurence
        last_occurence = -1
        left = 0
        right = n - 1
        while (left <= right):
            mid = (right + left) // 2

            if (arr[mid] == x):
                last_occurence = mid
                left = mid + 1

            elif (arr[mid] < x):
                left = mid + 1

            else:
                right = mid - 1
        return last_occurence - first_occurence + 1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x  = map(int, input().split())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
