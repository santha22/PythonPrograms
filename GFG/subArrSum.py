class Solution:
    def subArraySum(self, arr, n, s):

        current_sum = arr[0]
        start = 0

        for i in range(1, n + 1):
            while current_sum > s and start < i - 1:
                current_sum -= arr[start]
                start += 1

            if current_sum == s:
                return [start + 1, i]

            if i < n:
                current_sum += arr[i]

        return [-1]
def main():
    T = int(input())
    while(T>0):
        n = int(input())
        s = int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ans = ob.subArraySum(a,n,s)
        for i in ans:
            print(i,end= " ")
        print()
        T -=1

if __name__ == "__main__":
    main()

