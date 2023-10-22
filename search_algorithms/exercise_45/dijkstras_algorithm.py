#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from data_structures.exercise_50.graphs import BaseGraph
from typing import List, Dict, Union, Any
import heapq


class DijkstraAlgorithm:
    def __init__(
            self,
            numerical_string_list_helper: NumericStringListHelper,
            weighted_graph: BaseGraph
    ):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._weighted_graph = weighted_graph

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        return int(user_input)

    # Prints shortest paths from src to all other nodes
    def priority_queue_dijkstra(self, start_node: Union[int, float]) -> Dict[Union[int, float], Union[int, float]]:
        #  Initialise set to keep track of nodes that have been visited
        visited_nodes: set = set()

        # Initialise priority queue to store nodes that are being processed and push start node with distance of 0
        priority_queue_list: List = []
        heapq.heappush(priority_queue_list, (0, start_node))

        # Initialise node distances start node as 0 and infinite for all other nodes
        graph_nodes: Dict[Union[int, float], List[Dict]] = self._weighted_graph.nodes
        nodes_distances: Dict = {node: float('inf') for node in graph_nodes}
        nodes_distances[start_node] = 0

        while priority_queue_list:
            # Pop the node with the minimum distance from the priority queue and unpack both distance and node
            distance: Union[int, float]
            current_node: Union[int, float]
            distance, current_node = heapq.heappop(priority_queue_list)
            visited_nodes.add(current_node)

            # Iterate over all edges for current node
            for edge in graph_nodes.get(current_node):
                neighbour_node: Any = list(edge.keys())[0]
                weight: Union[int, float] = list(edge.values())[0]

                # Ensure edge weight is non-negative
                if weight < 0:
                    raise ValueError("Dijkstra's Algorithm can only be used with graphs that have non-negative weights")

                # Check if we have already visited neighbour_node
                if neighbour_node not in visited_nodes:
                    # Check if distance from current node to neighbour node is less than previously calculated shortest
                    # path
                    if nodes_distances[neighbour_node] > nodes_distances[current_node] + weight:
                        # Updating distance of neighbour node and push neighbour node onto priority queue
                        nodes_distances[neighbour_node] = nodes_distances[current_node] + weight
                        heapq.heappush(priority_queue_list, (nodes_distances[neighbour_node], neighbour_node))

        return nodes_distances
