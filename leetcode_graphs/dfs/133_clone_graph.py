# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node: Optional['Node'], seen: set, map: dict):
        if node.val in seen:
            return map[node.val]

        temp_node = Node(node.val)
        seen.add(node.val)
        map[node.val] = temp_node

        for neighbor in node.neighbors:
            temp_neighbor = self.dfs(neighbor, seen, map)
            temp_node.neighbors.append(temp_neighbor)

        return temp_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        seen = {set}
        map = {}
        return self.dfs(node, seen, map)
