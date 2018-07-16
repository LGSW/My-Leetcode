#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and
            self.isMatch(s.left, t.left) and
            self.isMatch(s.right, t.right))




a1 = TreeNode(4)
a2 = TreeNode(2)
a3 = TreeNode(6)
a4 = TreeNode(1)
a5 = TreeNode(3)
a6 = TreeNode(5)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6


x = Solution()
print(x.isSubtree(a1,a2))
