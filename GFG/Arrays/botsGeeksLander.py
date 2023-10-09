class Solution:
    def findBots(self, usernames, n):
        ans = []
        for username in usernames:
            evenChars = username[0::2]
            distinctChars = set(evenChars)
            lengthDistinctChars = len(distinctChars)

            flag = 0
            if lengthDistinctChars <= 1:
                flag = 1

            for i in range(2, int(lengthDistinctChars ** 0.5) + 1):
                if lengthDistinctChars % i == 0:
                    flag = 1
                    break

            ans.append(1 if flag == 0 else 0)
        return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        usernames = input().split()
        ob = Solution()
        print(*ob.findBots(usernames, n))
