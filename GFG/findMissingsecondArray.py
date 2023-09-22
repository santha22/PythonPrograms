def findMissing(a, b, n, m):
    mp = {}
    res = []
    for i in range(m):
        mp[b[i]] = 1 + mp.get(b[i], 0)

    for i in range(n):
        if a[i] not in mp:
            res.append(a[i])

    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = list(map(int, input().split()))
        n, m = s[0], s[1]
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        res = findMissing(a, b, n, m)
        for it in res:
            print(it, end=" ")