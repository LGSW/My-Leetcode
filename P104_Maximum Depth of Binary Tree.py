# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    maxdepth = 0
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tr(root, 1)
        return self.maxdepth

    def tr(self, node, depth):
        if not node:
            return
        if depth > self.maxdepth:
            self.maxdepth = depth
        self.tr(node.left, depth + 1)
        self.tr(node.right, depth + 1)


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t1.left = t2; t1.right = t3
t2.left = t4
t3.right = t5
t4.right = t6

x = Solution()
print(x.maxDepth(t1))