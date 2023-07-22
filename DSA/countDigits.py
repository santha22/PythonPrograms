def countDigits(x):
    res = 0
    while(x>0):
        x = x//10
        res += 1
    return res


if __name__ == "__main__":
    num = int(input())
    print(countDigits(num))
