class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for x in range(len(nums)):
            if (x%2==0):
                sum+=nums[x]
        return sum
