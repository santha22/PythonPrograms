class Solution:
    def zigZag(self, arr, n):
        flag = 1
        for i in range(n-1):
            if flag == 1:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

            flag = 1 - flag
        return arr


def main():
    T = int(input())

    while(T>0):
        n = int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.zigZag(a,n))
        T-=1

if __name__ == "__main__":
    main()

    