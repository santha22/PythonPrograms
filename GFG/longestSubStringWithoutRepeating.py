
class Solution:
    def longestUniqueSubsttr(self, s):
        dict = {}
        i,j = 0,0
        maxi = 0

        while(j<len(s)):

            if(s[j] in dict and dict[s[j]] >= i):
                i = dict[s[j]] + 1

            dict[s[j]] = j
            maxi = max(maxi, j-i+1)
            j+=1

        return maxi

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.longestUniqueSubsttr(s))
