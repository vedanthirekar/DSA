# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # flat = False
        def valid(root, start, end):
    
            if not root:
                return True
            if root.val<=start or root.val>=end:
                return False

            return valid(root.left,start,root.val) and valid(root.right, root.val,end)

        return valid(root,float("-inf"), float("inf"))

        # return True