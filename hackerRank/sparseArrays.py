n = int(input())
s = []
l = []
for i in range(n):
    s.append(input()).strip()


m = int(input())
for i in range(m):
    sub = input().strip()
    print(s.count(sub))
    

