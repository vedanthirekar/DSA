# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isBST(root,left_limit, right_limit):

            if not root: 
                return True

            # if not root.left and not  root.right:
            #     return True 

            # if root.left and not left_limit<root.left.val<root.val:
            #     return False

            # if root.right and not root.val<root.right.val <right_limit:
            #     return False


            # instead just compare the root
            if not left_limit < root.val < right_limit:
                return False


            return isBST(root.left, left_limit, root.val) and isBST(root.right, root.val, right_limit)

                

            
        return isBST(root, float("-inf"), float("inf"))