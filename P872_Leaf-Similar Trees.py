#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    list = []
    def treeseq(self, node):
        if not node:
            return
        if node.left == None and node.right == None:
            self.list.append(node.val)
        self.treeseq(node.left)
        self.treeseq(node.right)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.list = []
        self.treeseq(root1)
        list1 = self.list
        self.list = []
        self.treeseq(root2)
        if list1 == self.list:
            return True
        else:
            return False



x = Solution()

a1 =  TreeNode(1)
a2 =  TreeNode(2)
a3 =  TreeNode(3)
a4 =  TreeNode(4)
a5 =  TreeNode(5)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5

b1 =  TreeNode(1)
b2 =  TreeNode(2)
b3 =  TreeNode(3)
b4 =  TreeNode(4)
b5 =  TreeNode(5)
b1.left = b2
b1.right = b3
b3.left = b4
b3.right = b5

c1 = TreeNode(1)
c2 = TreeNode(1)
print(x.leafSimilar(a1, b1))
print(x.leafSimilar(c1, c2))
