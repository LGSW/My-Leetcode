#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        if t.left and t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        elif t.left and not t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        elif t.right and not t.left:
            return str(t.val) + '()' +  '(' + self.tree2str(t.right) + ')'
        else:
            return str(t.val)

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

b1 =  TreeNode(1)
b2 =  TreeNode(2)
b3 =  TreeNode(3)
b4 =  TreeNode(4)
b1.left = b2
b1.right = b3
b2.right = b4

x =  Solution()
print(x.tree2str(a1))
print(x.tree2str(b1))