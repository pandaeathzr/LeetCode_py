class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """


        """# Runtime: 48 ms, faster than 96.65% of Python3 online submissions for Unique Email Addresses."""

        end = []
        for email in emails:
            houzui = email.split("@")[-1]
            qianzui = email.split("+")[0]
            x = qianzui.split(".")
            sum=""
            for n in x:
                sum +=n
            sum =sum +"@"+houzui
            if(sum not in end):
                end.append(sum)
        return len(end)

if __name__=='__main__':
    result = Solution()
    result.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
