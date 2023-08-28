class Solution:
    def circularTour(self, lis , n):
        petrol = 0
        distance = 0

        for k in range(n):
            petrol += lis[k][0]
            distance += lis[k][1]

        if(petrol < distance):
            return -1

        balance = 0
        i = 0
        for j in range(n):
            balance += lis[j][0] - lis[j][1]
            if(balance < 0):
                i = j+1
                balance = 0

        return i

if __name__ == '__main__':
    t  = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        lis = []
        for i in range(1, 2*n, 2):
            lis.append([arr[i-1], arr[i]])
        print(Solution().circularTour(lis, n))