  class Solution:
    def increment(self, arr, n):
        # code here 
        carry = 1
        for i in range(n - 1, -1, -1):
           cur_sum = arr[i] + carry
           arr[i] = cur_sum % 10
           carry = cur_sum // 10

        if carry:
          arr.insert(0, carry)

        return arr
