class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        """Runtime: 20 ms, faster than 100.00% of Python online submissions for Hamming Distance."""
        return(bin(x^y).count("1"))
