#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans

class Solution(object):
    maxnum = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.maxnum

    def traverse(self, root):
        if not root:
            return 0
        left= self.traverse(root.left)
        right= self.traverse(root.right)
        self.maxnum = max(self.maxnum, left + right)
        return max(left, right)+1

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
print(x.diameterOfBinaryTree(a1))
