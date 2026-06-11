"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldtonew = {}
        def dfs(node):
            if not node:
                return

            if node in oldtonew:
                return oldtonew[node]
            
            new = Node(val = node.val)
            oldtonew[node] = new
            for nei in node.neighbors:
                neighbor = dfs(nei)
                if neighbor not in new.neighbors:
                    new.neighbors.append(neighbor)
            
            return new

        res = dfs(node)
        # print(node)
        return res