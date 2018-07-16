# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.convertBST(root.right)
        root.val += self.sum
        self.sum = root.val
        #print(root.val)
        self.convertBST(root.left)
        return root

    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum = 0
        myStack = []
        node = root
        while myStack or node:
            while node:
                myStack.append(node)
                node = node.right
            node = myStack.pop()
            s = sum
            sum += node.val
            node.val = node.val + s
            #print(node.val)
            node = node.left
        return root

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
print(x.convertBST(a1))