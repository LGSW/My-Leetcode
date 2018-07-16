#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.dic = dict()
        self.result = False
        def ft(root, k):
            if not root:
                return
            if self.dic.get(k - root.val):
                self.result = True
            self.dic[root.val] = k - root.val
            ft(root.left, k)
            ft(root.right, k)

        ft(root, k)
        return self.result


a1 =  TreeNode(2)
a2 =  TreeNode(1)
a3 =  TreeNode(3)
a4 =  TreeNode(4)
a5 =  TreeNode(7)
a1.left = a2
a1.right = a3
a2.right = a4
a3.right = a5

b1 =  TreeNode(2)
b2 =  TreeNode(3)
b1.right = b2

[4,2,null,-3,null,null,-1,null,0]
-3
c1 =  TreeNode(4)
c2 =  TreeNode(2)
c3 =  TreeNode(-3)
c4 =  TreeNode(-1)
c5 =  TreeNode(0)
c1.left = c2
c2.left = c4


x =  Solution()
print(x.findTarget(a1, 5))
print(x.findTarget(b1, 6))