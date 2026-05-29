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
        stk = [node]
        visited = set()
        oldtonew = {}
        while stk:
            og_node = stk.pop()
            if og_node not in visited:
                visited.add(og_node)
                new_node = Node(og_node.val)
                oldtonew[og_node] = new_node

            for nei in og_node.neighbors:
                if nei in visited:
                    oldtonew[og_node].neighbors.append(oldtonew[nei])
                    continue
                stk.append(nei)
                visited.add(nei)
                new_nei = Node(nei.val)
                oldtonew[nei] = new_nei
                oldtonew[og_node].neighbors.append(new_nei)

        return oldtonew[node]

