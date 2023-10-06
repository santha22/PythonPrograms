class Solution:

    # Function to reverse words in a given string.
    def reverseWords(self, S):
        # code here
        ls = list(reversed(S.split(".")))
        S = ""

        for i in range(len(ls)):
            if len(ls) - 1 != i:
                S += ls[i] + "."
            else:
                S += ls[i]

        return S

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.reverseWords(s))