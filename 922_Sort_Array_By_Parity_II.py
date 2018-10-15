class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        # Runtime: 148 ms, faster than 100.00% of Python online submissions for Sort Array By Parity II.
        """

        X = [x for x in A if x%2==0]
        Y = [y for y in A if y%2!=0]
        result=[]
        for i in range(len(X)):
            result.append(X[i])
            result.append(Y[i])

        return result

if __name__=='__main__':
    result = Solution()
    print(result.sortArrayByParityII([3,4]))
