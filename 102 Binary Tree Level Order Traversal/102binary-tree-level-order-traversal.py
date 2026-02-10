# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = [root]
        l = []
        while q:
            li = []
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                li.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            l.append(li)

        return l
                

        