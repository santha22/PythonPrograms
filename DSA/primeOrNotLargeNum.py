def prime(n):
    if(n==1):
        return False
    if(n==2 or n==3):
        return True
    if(n%2==0 or n%3==0):
        return False
    i = 5
    while(i*i<=n):
        if(n%i==0 or (n+2)%i==0):
            return False
        i+=6
    return True


n = int(input())
print(prime(n))