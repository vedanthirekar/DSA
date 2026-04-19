# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """if we find p<root<q or root == p or q, we return root as lca.
        else we go to one particular side
        """

        def lca(root):
            if p.val<root.val<q.val or p.val>root.val>q.val or p==root or q==root:
                return root
            elif root.val>p.val and root.val>q.val:
                return lca(root.left)
            else:
                return lca(root.right)

        return lca(root)
        