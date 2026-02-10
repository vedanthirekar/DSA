# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # maxx = [float("-inf")]

        count = [0]

        def traverse(root, maxx):
            if not root:
                return 

            if root.val>=maxx:
                count[0] +=1
                maxx = root.val

            traverse(root.left, maxx) 
            traverse(root.right, maxx)

        traverse(root, float("-inf"))
        return count[0]
