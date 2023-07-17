from collections import deque
class Solution:
    def FirstNonRepeating(self,A):
        dict = {}
        queue = deque()
        res = ""
        for i in A:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
            queue.append(i)

            while queue and dict[queue[0]] > 1:
                queue.popleft()

            if queue:
                res += queue[0]
            else:
                res += "#"

        return res

if __name__ == "__main__":
    t  = int(input())
    for i in range(t):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)