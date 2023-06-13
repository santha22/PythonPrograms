class Solution:
    def firstRepChar(self, s):
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
                return i
            else:
                count[i] = 1

        return -1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.firstRepChar(s))
