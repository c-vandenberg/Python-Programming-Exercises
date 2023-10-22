#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from data_structures.exercise_46.queues import GenericFifoQueue
from data_structures.exercise_50.graphs import DirectedGraph
from data_structures.exercise_50.graphs import UndirectedGraph
from dijkstras_algorithm import DijkstraAlgorithm
from typing import Dict, Union


def main():
    numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    fifo_queue: GenericFifoQueue = GenericFifoQueue()
    weighted_undirected_graph: UndirectedGraph = UndirectedGraph(fifo_queue)

    weighted_undirected_graph.add_node(32)
    weighted_undirected_graph.add_node(38)
    weighted_undirected_graph.add_node(49)
    weighted_undirected_graph.add_node(52)
    weighted_undirected_graph.add_node(56)
    weighted_undirected_graph.add_node(61)
    weighted_undirected_graph.add_node(65)
    weighted_undirected_graph.add_node(73)

    weighted_undirected_graph.add_edge(32, 38, 8)
    weighted_undirected_graph.add_edge(32, 61, 4)
    weighted_undirected_graph.add_edge(32, 73, 1)
    weighted_undirected_graph.add_edge(38, 49, 12)
    weighted_undirected_graph.add_edge(38, 73, 15)
    weighted_undirected_graph.add_edge(38, 52, 6)
    weighted_undirected_graph.add_edge(49, 52, 3)
    weighted_undirected_graph.add_edge(52, 56, 2)
    weighted_undirected_graph.add_edge(61, 65, 6)
    weighted_undirected_graph.add_edge(73, 56, 35)
    weighted_undirected_graph.add_edge(73, 65, 1)

    dijkstra_algorithm: DijkstraAlgorithm = DijkstraAlgorithm(numeric_string_helper, weighted_undirected_graph)

    nodes_distances: Union[Dict, int, float] = dijkstra_algorithm.priority_queue_dijkstra(32)

    for node in nodes_distances:
        print(f"{node} \t\t {nodes_distances[node]}")


if __name__ == '__main__':
    main()
