# 210. Course Schedule II
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
# you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers,
# return any of them. If it is impossible to finish all courses, return an empty array.
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        queue = deque()

        for edge in prerequisites:
            destination, source = edge
            graph[source].append(destination)

            indegrees[destination] += 1

        for node in range(numCourses):
            if node not in indegrees.keys():
                queue.append(node)

        while queue:
            source = queue.popleft()
            result.append(source)

            for neighbor in graph[source]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) == numCourses:
            return result

        return []


if __name__ == "__main__":
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]

    solution = Solution()
    print(solution.findOrder(numCourses, prerequisites))
