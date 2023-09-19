class Solution:
    def NumberofElementsInIntersection(self, a, b, n, m):
        # return: expected length of the intersection array.

        # code here
        hasha = {}
        for i in a:
            hasha[i] = 1 + hasha.get(i, 0)

        hashb = {}
        for j in b:
            hashb[j] = 1 + hashb.get(j, 0)

        count = 0

        if (len(hasha) < len(hashb)):
            for i in hasha:
                if i in hashb:
                    count += 1

        else:
            for i in hashb:
                if i in hasha:
                    count += 1

        return count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.NumberofElementsInIntersection(a,b,n,m))