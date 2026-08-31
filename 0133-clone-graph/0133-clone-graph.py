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
        
        clones = {}

        if not node:
            return None
        def clone(node):

            if node in clones:
                return clones[node]

            clone_node = Node()
            clone_node.val = node.val
            
            clones[node] = clone_node

            for neighbor_node in node.neighbors:
                # if neighbor_node not in seen:
                    clone_node.neighbors.append(clone(neighbor_node))

            return clone_node

        return clone(node)