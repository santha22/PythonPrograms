from collections import defaultdict


class Solution:
    def groupAnagrams(self, s):
        # Code here

        res = defaultdict(list)

        for strs in s:
            count = [0] * 26

            for c in strs:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(strs)

        ans = []
        for strs in res.values():
            ans.append(sorted(strs))

        ans.sort()

        return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(input().split())
        obj = Solution()
        ans = obj.groupAnagrams(a)
        for i in ans:
            for j in i:
                print(j, end=" ")
