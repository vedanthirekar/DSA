# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        
        res = []
        def dfs(root, curr_sum, path):
            if not root:
                return 
            
            if curr_sum + root.val == targetSum and not root.right and not root.left:
                path.append(root.val)
                res.append(path.copy())
                path.pop()
                return
                
            path.append(root.val)
            dfs(root.right, curr_sum+root.val,path)
            dfs(root.left, curr_sum + root.val, path)
            path.pop()


        dfs(root, 0, [])
        return res
        