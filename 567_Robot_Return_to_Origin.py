class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u,d,l,r =0,0,0,0
        for chr in moves:
            if(chr=="U"):
                u+=1
            elif(chr=="D"):
                d+=1
            elif(chr=="L"):
                l+=1
            elif(chr=="R"):
                r+=1
        if(r==l and u==d):
            return True
        return False


if __name__=='__main__':
    result = Solution()
    # words = []
    # for i in range(3):
    #     words.append(input())
    # print(result.uniqueMorseRepresentations(words))
    print(result.judgeCircle("UD"))
