import heapq
from collections import Counter
class Solution:
    def rearrangeString(self, s):
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=="-1":
            print(0)
        elif sorted(str1) != sorted(str2):
            print(0)
        else:
            for i in range(len(str2) - 1):
                if str2[i] == str2[i+1]:
                    print(0)
                    break
            else:print(1)