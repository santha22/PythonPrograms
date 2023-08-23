class Solution:
    def longestKSubstr(self, s, k):
        strdict = {}
        i,j = 0,0
        maxi = -1

        while(j<len(s)):

            if(s[j] in strdict):
                strdict[s[j]] += 1
            elif(s[j] not in strdict):
                strdict[s[j]] = 1

            if(len(strdict) == k):
                maxi = max(maxi, j - i + 1)

            elif(len(strdict) > k):
                while(len(strdict) > k):

                    strdict[s[i]] -= 1
                    if(strdict[s[i]] == 0):
                        strdict.pop(s[i])
                    i+=1

            j+=1

        return maxi

if __name__ == '__main__':
    j = int(input())
    for i in range(j):
        s = input()
        k = int(input())
        ob = Solution()
        print(ob.longestKSubstr(s,k))