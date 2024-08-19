# 332. Reconstruct Itinerary
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and
# the arrival airports of one flight. Reconstruct the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple
# valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
#
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
from collections import defaultdict
from typing import List


class Solution:
    graph = None

    def build_graph(self, tickets: List[List[str]]):
        self.graph = defaultdict(list)

        # build adjacency list
        for ticket in tickets:
            source, destination = ticket
            self.graph[source].append(destination)

        # sort the neighbors
        for node in self.graph:
            self.graph[node].sort()

    def dfs(self, source, result, seen):
        for neighbor in self.graph[source]:
            ticket = (source, neighbor)
            if ticket not in seen:
                seen.add(ticket)
                result.append(neighbor)
                self.dfs(neighbor, result, seen)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.build_graph(tickets)
        source = "JFK"
        result = [source]
        seen = {set}
        self.dfs(source, result, seen)
        return result


if __name__ == "__main__":
    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(Solution().findItinerary(tickets))
