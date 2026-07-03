# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        maxx = float('-inf')

        def dfs(node, maxx):
            if not node:
                return 
            if node.val>=maxx:
                maxx = node.val
                count[0] +=1

            dfs(node.left, maxx)
            dfs(node.right, maxx)


        dfs(root, maxx)

        return count[0]
        