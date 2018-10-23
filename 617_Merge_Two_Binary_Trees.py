# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # if(t1 != None and t2!= None):
        #     t1.val += t2.val
        #     self.mergeTrees(t1.left,t2.left)
        #     self.mergeTrees(t1.right,t2.right)
        # elif(t1==None):
        #     t1 = t2   #前半部分无法连接

        """Runtime: 176 ms, faster than 10.55% of Python3 online submissions for Merge Two Binary Trees."""
        if(t1 == None):
            return t2
        if(t2 == None):
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)

        return t1
if __name__=='__main__':
    result = Solution()
    t1 =TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    t2 =TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    x = result.mergeTrees(t1,t2)
    print(x.left.right.val)
