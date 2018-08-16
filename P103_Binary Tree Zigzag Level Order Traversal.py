# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def traverse(root, depth, ans):
            if not root:
                return
            if len(ans) <= depth:
                ans.append([root.val])
            elif not depth % 2:
                ans[depth].extend([root.val])
            else:
                ans[depth].insert(0, root.val)
            traverse(root.left, depth + 1, ans)
            traverse(root.right, depth + 1, ans)

        ans = []
        traverse(root, 0, ans)  # level from 0
        return ans


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
print(x.zigzagLevelOrder(t1))