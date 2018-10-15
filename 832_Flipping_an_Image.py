class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        # Runtime: 36 ms, faster than 90.93% of Python online submissions for Flipping an Image.
        """
        result = []
        for item in A:
            temp = item[::-1]
            for i in range(len(temp)):
                if(temp[i]==0):
                    temp[i]=1
                else:
                    temp[i]=0
            result.append(temp)
        return result

if __name__=='__main__':
    result = Solution()
    print(result.flipAndInvertImage([[1,0]]))
