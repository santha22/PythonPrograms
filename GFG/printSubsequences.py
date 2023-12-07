def f(ind, s, res, current_subsequence):
    if ind == len(s):
        res.append(''.join(current_subsequence))
        return

    # take
    current_subsequence.append(s[ind])
    f(ind + 1, s, res, current_subsequence)

    # not take
    current_subsequence.pop()
    f(ind + 1, s, res, current_subsequence)

def printSubsequences(s):
    res = []
    current_subsequence = []
    f(0, s, res, current_subsequence)
    return res



s = input()
res = printSubsequences(s)
for i in res:
    print(i)
