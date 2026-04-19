# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """will try by checking if both sides return or only one side returns.
        base condition will be if we find p or q return it
        """

        # def lca(root):
        #     if not root:
        #         return None
        #     if root == p or root == q:
        #         return root
        #     elif lca(root.right) and lca(root.left):
        #         return root
        #     elif lca(root.right):
        #         return root.right
        #     elif lca(root.left):
        #         return root.left
            
        # return lca(root)


        def dfs(node):
            if not node:
                return None
            if node is p or node is q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right

        return dfs(root)