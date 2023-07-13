
from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        frequency = {}
        
        for i in arr:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        seen_frequency = set()
        for freq in frequency.values():
            if freq in seen_frequency:
                return False
            seen_frequency.add(freq)
        
        return True

class IntArray:
  def __init__(self):
    pass
  def Input(self,n):
    arr = [int(i) for i in input().strip().split()] 
    return arr
  def Print(self, arr):
    for i in arr:
      print(i, end=" ")
    print()

if __name__ == "__main__":
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = IntArray().Input(n)
    obj = Solution()
    res = obj.isFrequencyUnique(n, arr)
    result_val = 1 if res else 0
    print(result_val)
        
