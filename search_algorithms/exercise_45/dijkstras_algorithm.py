#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from data_structures.exercise_50.graphs import DirectedGraph
from data_structures.exercise_46.queues import GenericPriorityQueue
from typing import List, Union
import random
import heapq


class DijkstrasAlgorithm:
    def __init__(
            self,
            numerical_string_list_helper: NumericStringListHelper,
            weighted_directed_graph: DirectedGraph,
            priority_queue: GenericPriorityQueue
    ):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._weighted_directed_graph = weighted_directed_graph
        self._priority_queue = priority_queue

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        return int(user_input)

    # Prints shortest paths from src to all other vertices
    def priority_queue_dijkstra_shortest_path(self, start_node: Union[int, float]):
        # Create a priority queue to store vertices that
        # are being preprocessed
        priority_queue_list: List = []
        self._priority_queue.enqueue(priority_queue_list, ())
        heapq.heappush(priority_queue_list, (0, start_node))

        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[start_node] = 0

        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)

            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        # Print shortest distances stored in dist[]
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
