

class Solution:
    def firstElementKTime(self, a, n, k):
        # code here
        count = {};
        for i in range(0, n):
            if (a[i] in count.keys()):
                count[a[i]] += 1

            else:
                count[a[i]] = 1
            if (count[a[i]] == k):
                return a[i]

        return -1

def main():
    T = int(input())

    while(T>0):
        s=[int(x) for x in input().strip().split()]
        n,k=s[0],s[1]
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a,n,k))
        T-=1

if __name__ == "__main__":
    main()

