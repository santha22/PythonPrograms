def palindromeNum(x):
    val = x
    rev = 0
    while(val > 0):
        rev = (rev * 10) + (val % 10)
        val = val // 10

    if(rev == x):
        return  True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    print(palindromeNum(n))