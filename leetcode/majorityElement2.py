class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashm = {}
        majority = []
        
        n = len(nums)
        for i in range(n):
            hashm[nums[i]] = 1 + hashm.get(nums[i], 0)

        for i in hashm:
            if(hashm[i] > n//3):
                majority.append(i)

        
        return majority
