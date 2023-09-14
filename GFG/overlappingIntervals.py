class Solution:
    def overlappedInterval(self, arr):
        # Code here
        n = len(arr)
        ans = []
        arr.sort()
        start = arr[0][0]
        end = arr[0][1]

        for i in range(1, n):
            if (end >= arr[i][0]):
                end = max(end, arr[i][1])

            else:
                ans.append([start, end])
                start = arr[i][0]
                end = arr[i][1]

        ans.append([start, end])
        return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        arr = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            arr.append([x,y])

        ob = Solution()
        ans = ob.overlappedInterval(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")

        print()