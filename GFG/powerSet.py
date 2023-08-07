class Solution:
    def generate(self, s, current, index, result):
        if (index == len(s)):
            if current:
                result.append(current)
            return
        self.generate(s, current + s[index], index + 1, result)
        self.generate(s, current, index + 1, result)

    def AllPossibleStrings(self, s):
        # Code here
        result = []
        self.generate(s, "", 0, result)
        result.sort()
        return result



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str = input()
        ob = Solution()
        ans = ob.AllPossibleStrings(str)
        for i in ans:
            print(i, end=" ")
        print()