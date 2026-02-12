# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        lca = [root]
        
        def search(node):
            if not node:
                return 

            lca[0] = node

            if root is p or root is q:
                return 
            elif node.val<q.val and node.val<p.val:
                return search(node.right)
            elif node.val>q.val and node.val>p.val:
                return search(node.left)
            else:
                return 

        search(root)
        return lca[0]