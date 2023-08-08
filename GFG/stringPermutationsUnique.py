"""from itertools import permutations
class Solution:
    def permutations(self, s, i, n, result):
        if (i == n - 1):
            result.append(''.join(s))
            return
        j = i
        while (j < n):
            s[i], s[j] = s[j], s[i]
            self.permutations(s[:], i + 1, n, result)
            s[i], s[j] = s[j], s[i]
            j += 1


    def find_permutation(self, s):
        # Code here
        result = []
        self.permutations(list(s), 0, len(s), result)
        result = list(set(result))
        result.sort()
        return result"""

class Solution:
    def recurPermute(self,s,ds,ans,freq):
        if(len(ds) == len(s)):
            ans.append(''.join(ds))
            return
        for i in range(len(s)):
            if(freq[i]==0):
                freq[i] = 1
                ds.append(s[i])
                self.recurPermute(s,ds,ans,freq)
                ds.pop()
                freq[i] = 0
    
    
    def find_permutation(self,s):
        ans = []
        ds = []
        freq = [0]*len(s)
        self.recurPermute(s,ds,ans,freq)
        ans = list(set(ans))
        ans.sort()
        return ans
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        ans = ob.find_permutation(s)
        for i in ans:
            print(i, end=" ")
        print()
