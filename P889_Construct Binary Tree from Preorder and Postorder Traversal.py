# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return
        node = TreeNode(pre[0])
        pre = pre[1:]; post = post[:-1]
        k = 0
        if len(pre) > 0:
            for i in range(len(post)):
                if post[i] == pre[0]:
                    k = i
                    break
        node.left = self.constructFromPrePost(pre[:k+1], post[:k+1])
        node.right = self.constructFromPrePost(pre[k+1:], post[k+1:])
        return node

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t1.left = t2; t1.right = t3
t2.left = t4; t2.right = t5
t3.left = t6; t3.right = t7

x = Solution()
print((x.constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])))

