#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    dep = []

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)

        return [s / float(c) for s, c in info]

a1 =  TreeNode(2)
a2 =  TreeNode(1)
a3 =  TreeNode(3)
a4 =  TreeNode(4)
a5 =  TreeNode(7)
a1.left = a2
a1.right = a3
a2.right = a4
a3.right = a5


x = Solution()
print(x.averageOfLevels(a1))