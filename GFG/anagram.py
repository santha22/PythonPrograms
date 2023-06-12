class Solution:
    def isAnagram(self,a,b):
        a=list(a)
        a.sort()
        """print(a.sort())
        print(b.sort())"""
        b=list(b)
        b.sort()
        if a == b:
            return True
        else:
            return False

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a,b = map(str, input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO")
