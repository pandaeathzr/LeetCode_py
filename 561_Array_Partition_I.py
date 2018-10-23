class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """Runtime: 124 ms, faster than 65.02% of Python3 online submissions for Array Partition I."""
        nums.sort()
        sum = 0
        for x in range(len(nums)):
            if (x%2==0):
                sum+=nums[x]
        return sum
