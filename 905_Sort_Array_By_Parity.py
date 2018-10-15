class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """# Runtime: 60 ms, faster than 90.05% of Python online submissions for Sort Array By Parity."""
        return ([x for x in A if x%2==0]+[x for x in A if x%2!=0])
