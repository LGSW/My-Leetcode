# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def getMinimumDifference(self, root):
        nums = self.inorder(root)
        return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []


    prev = None
    minnum = 9999999
    def getMinimumDifference1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        self.getMinimumDifference(root.left)
        if (self.prev!= None):
            self.minnum = min(self.minnum, root.val - self.prev)
        self.prev = root.val
        self.getMinimumDifference(root.right)
        return self.minnum

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
print(x.getMinimumDifference(a1))
