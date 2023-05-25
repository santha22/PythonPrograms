def isSortedBetter(a, si):
    l = len(a)
    if si == l-1 or si==l:
        return True
    if a[si]> a[si+1]:
        return False
    isSmallerPartSorted = isSortedBetter(a, si+1)
    return isSmallerPartSorted

a = list(map(int, input().split()))
print(isSortedBetter(a,0))
