class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        """#Runtime: 88 ms, faster than 44.06% of Python3 online submissions for Self Dividing Numbers."""
        result = []
        list = range(left,right+1)

        for x in list:
            flag = 0
            for y in str(x):
                if(y == '0' or x % int(y) !=0 ):
                    flag =1
                    break

            if(flag == 0):
                result.append(x)

        return result

if __name__=='__main__':
    result = Solution()
    print(result.selfDividingNumbers(1,22))
