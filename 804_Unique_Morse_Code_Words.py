class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        """# Runtime: 40 ms, faster than 14.24% of Python online submissions for Unique Morse Code Words."""
        change = []
        morsec=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for item in words:
            word =[]
            for c in item:
                print(c)
                word.append(morsec[ord(c)-97])
            change.append(''.join(word))
        change = list(set(change))
        return len(change)

if __name__=='__main__':
    result = Solution()
    # words = []
    # for i in range(3):
    #     words.append(input())
    # print(result.uniqueMorseRepresentations(words))
    print(result.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
