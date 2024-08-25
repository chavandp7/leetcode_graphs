# topological sort algorithm
# Time complexity - O(V + E)
# Space complexity - O (V) for queue and indegree

from collections import defaultdict, deque


def topological_sort(edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    queue = deque()

    # 1. build graph and calculate indegrees - O(E)
    for i in range(len(edges)):
        source, destination = edges[i]
        graph[source].append(destination)

        indegree[destination] += 1

    # 2. append nodes with indgeree 0 in queue - O(V)
    for node in graph:
        if node not in indegree.keys():
            queue.append(node)

    topological_sorted_order = []

    # 3. pop node from queue and add it to topologically sorted order
    # 4. Decrease indegree for neighbors of the popped node
    # 5. If the indegree of neighbor becomes 0 then add it to queue
    # O(V + E)
    while queue:
        node = queue.popleft()
        topological_sorted_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    print(topological_sorted_order)


if __name__ == "__main__":
    num = 10
    edges = [
        ['A', 'B'],
        ['A', 'F'],
        ['B', 'H'],
        ['G', 'A'],
        ['G', 'B'],
        ['G', 'C'],
        ['D', 'C'],
        ['D', 'E'],
        ['D', 'I'],
        ['D', 'H'],
        ['I', 'C'],
        ['E', 'I'],
        ['J', 'E']
    ]
    topological_sort(num, edges)
