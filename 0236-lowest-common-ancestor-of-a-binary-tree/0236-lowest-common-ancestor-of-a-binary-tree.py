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

        def lca(root):
            if not root:
                return None
            elif root == p or root == q:
                return root
            left = lca(root.left)
            right = lca(root.right)
            elif left and right
                return root
            if left:
                return left 
            else:
                return right
            
        return lca(root)


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