def maximize(n, x):
    # write your code here
    arr = x[::-1]
    print(arr)
    sum = 0
    for i in range(len(arr)):
        sum += (arr[i]-i)**2
        print(arr[i])
    print(sum)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        x = list(map(int, input().split()))
        maximize(n,x)