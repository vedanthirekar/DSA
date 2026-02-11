# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        count = [0]
        def traverse(root):
            
            if not root:
                return

            traverse(root.left)
            count[0] +=1
            if count[0] == k:
                ans[0] = root.val
                return 
            
            if count[0] <k:
                traverse(root.right)

        traverse(root)
        return ans[0]

            
        