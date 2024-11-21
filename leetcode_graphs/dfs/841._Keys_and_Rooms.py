# 841. Keys and Rooms
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it,
# denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
# return true if you can visit all the rooms, or false otherwise.
from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        n = len(rooms)

        for index in range(n):
            neighbors = rooms[index]
            for neighbor in neighbors:
                graph[index].append(neighbor)

        def dfs(room):
            if room in visited:
                return

            visited.add(room)

            for key in graph[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)

        for room in range(n):
            if room not in visited:
                return False

        return True


if __name__ == "__main__":
    # rooms = [[1, 3], [3, 0, 1], [2], [0]]
    rooms = [[1], [2], [3], []]
    solution = Solution()
    print(f"can visit all rooms - {solution.canVisitAllRooms(rooms)}")
