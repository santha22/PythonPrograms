def f(i):
    if(i>=len(s)//2):
        return True
    if(s[i] != s[len(s)-i-1]):
        return False
    return f(i+1)


s = input()
print(f(0))
