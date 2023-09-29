from typing import List


class Solution:
    def convertToWave(self, n, a):
        # code here
        for i in range(n):
            if i + 1 < n:
                if i % 2 == 0:
                    a[i], a[i + 1] = a[i + 1], a[i]

                    




