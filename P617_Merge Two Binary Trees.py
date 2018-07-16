#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees1(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        newtree = TreeNode(0)
        newtree.val = t1.val + t2.val
        def traverse(t1, t2, nt):
            nt.val = t1.val +  t2.val
            if t1.left and t2.left:
                nt.left = TreeNode(0)
                traverse(t1.left, t2.left, nt.left)
            elif t1.left and not t2.left:
                nt.left = TreeNode(0)
                t2.left = TreeNode(0)
                traverse(t1.left, t2.left, nt.left)
            elif not t1.left and t2.left:
                nt.left = TreeNode(0)
                t1.left = TreeNode(0)
                traverse(t1.left, t2.left, nt.left)

            if t1.right and t2.right:
                nt.right = TreeNode(0)
                traverse(t1.right, t2.right, nt.right)
            elif t1.right and not t2.right:
                nt.right = TreeNode(0)
                t2.right = TreeNode(0)
                traverse(t1.right, t2.right, nt.right)
            elif not t1.right and t2.right:
                nt.right = TreeNode(0)
                t1.right = TreeNode(0)
                traverse(t1.right, t2.right, nt.right)
            if not t1.left and not t2.left and not t1.right and not t2.right:
                return

        traverse(t1,t2,newtree)
        return newtree

a1 =  TreeNode(2)
a2 =  TreeNode(1)
a3 =  TreeNode(3)
a4 =  TreeNode(4)
a5 =  TreeNode(7)
a1.left = a2
a1.right = a3
a2.right = a4
a3.right = a5

b1 =  TreeNode(1)
b2 =  TreeNode(3)
b3 =  TreeNode(2)
b4 =  TreeNode(5)
b1.left = b2
b1.right = b3
b2.left = b4

x =  Solution()
a = (x.mergeTrees(a1,b1))

def preoder(node):
    if not node:
        return
    print(node.val)
    preoder(node.left)
    preoder(node.right)

preoder(a)


