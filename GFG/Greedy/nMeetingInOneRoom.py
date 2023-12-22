
def maximumMeetings(start: List[int], end: List[int]) -> int:
    # write your code here
    ans = []
    n = len(start)
    for i in range(n):
        ans.append([start[i], end[i]])

    ans.sort(key = lambda x: x[1])

    length = 1
    last = ans[0][1]
    
    for i in range(n):
        if ans[i][0] > last:
            length += 1
            last = ans[i][1]

    return length
