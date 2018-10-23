class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # max = -10000
        # for x in range(len(A)):
        #     if(max<=A[x]):
        #         max = A[x]
        #     else:
        #         return x-1

        # """Runtime: 40 ms, faster than 85.29% of Python3 online submissions for Peak Index in a Mountain Array."""
        # for i in range(len(A)):
        #     if (A[i] > A[i+1]):
        #         return i

        """Complexity Analysis:
            Time Complexity: O(logN), where N is the length of A.
            Space Complexity: O(1).
        """

        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = int((lo + hi) / 2)
            if (A[mi] < A[mi + 1]):
                lo = mi + 1
            else:
                hi = mi
        return lo

if __name__=='__main__':
    result = Solution()
    print(result.peakIndexInMountainArray([1,2,3,4,5,4,3,2,1]))
