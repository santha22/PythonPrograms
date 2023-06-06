class Solution:
    def sort012(self,arr,n):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if arr[i] == 0:
                cnt0 += 1

            elif arr[i] == 1:
                cnt1 += 1

            elif arr[i] == 2:
                cnt2 += 1

        i = 0
        while (cnt0 > 0):
            arr[i] = 0
            i += 1
            cnt0 -= 1

        while (cnt1 > 0):
            arr[i] = 1
            i += 1
            cnt1 -= 1

        while (cnt2 > 0):
            arr[i] = 2
            i += 1
            cnt2 -= 1

        return arr

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end = ' ')
        print()


