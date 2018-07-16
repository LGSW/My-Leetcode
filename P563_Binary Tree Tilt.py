#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        def nodesum(root):
            if not root: return 0
            leftsum = nodesum(root.left)
            rightsum = nodesum(root.right)
            self.sum += abs(leftsum - rightsum)
            return leftsum + rightsum + root.val
        nodesum(root)
        return self.sum

a1 =  TreeNode(4)
a2 =  TreeNode(2)
a3 =  TreeNode(6)
a4 =  TreeNode(1)
a5 =  TreeNode(3)
a6 =  TreeNode(5)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6

x =  Solution()
print(x.findTilt(a1))