class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        ##Your code here
        curSum = 0
        msf = arr[0]
        for i in range(N):
            curSum += arr[i]
            if msf < curSum:
                msf = curSum
            if curSum < 0:
                curSum = 0

        return msf
