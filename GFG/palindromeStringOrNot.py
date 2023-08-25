class Solution:
    def palindrome(self, s):
        i,j = 0,len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                return 0
        return 1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.palindrome(s))