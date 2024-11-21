from collections import defaultdict
from typing import List


def traverse_graph(matrix: List[List[int]]) -> None:
    def dfs(node):
        if node in seen:
            return

        seen.add(node)

        for neighbor in graph[node]:
            if neighbor not in seen:
                print(f"visited node {neighbor}")
                dfs(neighbor)

    n = len(matrix)
    graph = defaultdict(list)

    # populate adjacency list for graph representation
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    seen = set()

    for i in range(n):
        if i not in seen:
            print(f"visited node {i}")
            dfs(i)
