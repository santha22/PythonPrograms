"""class Solution:
    def insert(self, q, k):
        q.insert(0,k)



    def findFrequency(self, q, k):
        freq = 0
        size = len(q)
        while (size):
            size -= 1

            x = q.pop()
            if (x == k):
                freq += 1


            q.insert(0, x)
            #print("queue is",q)
        return freq
"""

class Solution:
    def insert(self, q, k):
        q.append(k)

    def findFrequency(self, q, k):

freq = 0
        for num in q:
            if num == k:
                freq += 1

        return freq


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        obj = Solution()
        q = []
        n = int(input())
        arr = list(map(int, input().strip().split()))
        for k in arr:
            obj.insert(q,k)

        m = int(input())
        query = list(map(int, input().strip().split()))
        for k in query:
            f = obj.findFrequency(q,k)
            if f!=0:
                print(f)
            else:
                print(-1)