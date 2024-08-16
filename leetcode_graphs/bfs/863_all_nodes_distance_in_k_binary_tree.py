# 863. All Nodes Distance K in Binary Tree
# Given the root of a binary tree, the value of a target node target,
# and an integer k, return an array of the values of all nodes that have a distance k
# from the target node.
#
# You can return the answer in any order.
# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build_graph(root: TreeNode):
            if not root:
                return

            value = root.val
            if root.left:
                graph[value].append(root.left.val)
                graph[root.left.val].append(value)
                build_graph(root.left)

            if root.right:
                graph[value].append(root.right.val)
                graph[root.right.val].append(value)
                build_graph(root.right)

        graph = defaultdict(list)
        build_graph(root)

        seen = {target.val}
        queue = deque([target.val])
        level = 0
        result = []

        while queue:
            size = len(queue)

            if level == k:
                while queue:
                    result.append(queue.popleft())
                return result

            for i in range(size):
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

            level += 1

        return result


if __name__ == "__main__":
    root = TreeNode(3)

    node_1 = TreeNode(5)
    node_2 = TreeNode(1)

    node_3 = TreeNode(6)
    node_4 = TreeNode(2)

    node_5 = TreeNode(0)
    node_6 = TreeNode(8)

    node_7 = TreeNode(7)
    node_8 = TreeNode(4)

    root.left = node_1
    root.right = node_2

    node_1.left = node_3
    node_1.right = node_4

    node_2.left = node_5
    node_2.right = node_6

    node_4.left = node_7
    node_4.right = node_8

    ans = Solution().distanceK(root, node_1, 2)
    print(ans)
