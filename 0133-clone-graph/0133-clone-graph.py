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
        if not node:
            return None

        # visited = set()
        hmap = {}
        def dfs(node):
            if node in hmap:
                return hmap[node]

            # visited.add(node)
            clone_node = Node(val = node.val)
            hmap[node] = clone_node

            for nei in node.neighbors:
                clone_nei = dfs(nei)
                clone_node.neighbors.append(clone_nei)
            
            return clone_node
            
        return dfs(node)