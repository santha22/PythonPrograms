from itertools import permutations
class Solution:
    def permutations(self, s):
        ans = list(permutations(s))
        ans = [''.join(t) for t in ans]
        ans.sort()
        return ans

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        ans = ob.permutations(s)
        for i in ans:
            print(i, end=" ")
        print()