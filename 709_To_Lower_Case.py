class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        """# Runtime: 24 ms, faster than 30.92% of Python online submissions for To Lower Case."""
        #return str.lower()

        """# Runtime: 20 ms, faster than 91.82% of Python online submissions for To Lower Case."""
        s1 = list(str)
        d = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i',
         'J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s',
         'T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
        for i in range(len(str)):
            if str[i] in d:  #key
                s1[i] = d[str[i]]

        """https://www.cnblogs.com/jsplyy/p/5634640.html
        'sep'.join(seq)：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
        sep：分隔符。可以为空
        seq：要连接的元素序列、字符串、元组、字典
        """
        return ''.join(s1)


if __name__ =='__main__':
    result = Solution()
    str = input()
    print(result.toLowerCase(str))
