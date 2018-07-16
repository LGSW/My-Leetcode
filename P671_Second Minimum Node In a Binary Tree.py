#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min1 = 1e9;
        self.min2 = 1e9
        def findmin(root):
            if not root:
                return
            if root.val != self.min1 and root.val != self.min2:
                if root.val < self.min1:
                    self.min2 = self.min1
                    self.min1 = root.val
                else:
                    self.min2 = min(self.min2, root.val)
            findmin(root.left)
            findmin(root.right)

        findmin(root)
        if self.min2 != 1e9:
            return self.min2
        return -1



a1 =  TreeNode(2)
a2 =  TreeNode(1)
a3 =  TreeNode(3)
a4 =  TreeNode(4)
a5 =  TreeNode(7)
a1.left = a2
a1.right = a3
a2.right = a4
a3.right = a5

x =  Solution()
print(x.findSecondMinimumValue(a1))
