"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        seen = dict()

        def dfs_copy(node):
            if not node:
                return
            if node.val in seen:
                return seen[node.val]

            neighbors = []
            copy_node = Node(node.val, neighbors)
            seen[node.val] = copy_node

            for neighbor in node.neighbors:
                neighbors.append(dfs_copy(neighbor))

            return copy_node

        return dfs_copy(node)