class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # #Runtime: 28 ms, faster than 46.31% of Python online submissions for Jewels and Stones.
        # jewels = {c for c in J}
        # result =[]
        # for c in S:
        #     result.append(c in jewels)
        # return(sum(result))

        #Runtime: 24 ms, faster than 91.19% of Python online submissions for Jewels and Stones.
        print([c in jewels for c in S])
        return sum([c in jewels for c in S])

if __name__ == "__main__":
    result= Solution()
    J = input()
    S = input()
    print(result.numJewelsInStones(J,S))
