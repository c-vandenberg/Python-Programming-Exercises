#!/usr/bin/env python3

from graphs import DirectedGraph, UndirectedGraph
from typing import Union, List, Set


def main():
    # Create directed graph
    my_directed_graph = DirectedGraph()

    # Add nodes
    my_directed_graph.add_node("A")
    my_directed_graph.add_node("B")
    my_directed_graph.add_node("C")
    my_directed_graph.add_node("D")
    my_directed_graph.add_node("E")
    my_directed_graph.add_node("F")
    my_directed_graph.add_node("G")
    my_directed_graph.add_node("H")
    my_directed_graph.add_node("I")

    # Add edges
    my_directed_graph.add_edge("A", "B")
    my_directed_graph.add_edge("B", "C")
    my_directed_graph.add_edge("E", "G")
    my_directed_graph.add_edge("G", "A")



    directed_graph_connected_nodes: Set = my_directed_graph.connected_components()

    directed_has_cycles: bool = my_directed_graph.is_cyclic()

    # Create undirected graph
    my_undirected_graph = UndirectedGraph()

    # Add nodes
    my_undirected_graph.add_node("A")
    my_undirected_graph.add_node("B")
    my_undirected_graph.add_node("C")
    my_undirected_graph.add_node("D")
    my_undirected_graph.add_node("E")
    my_undirected_graph.add_node("F")
    my_undirected_graph.add_node("G")
    my_undirected_graph.add_node("H")
    my_undirected_graph.add_node("I")

    # Add edges
    my_undirected_graph.add_edge("A", "B")
    my_undirected_graph.add_edge("B", "C")
    my_undirected_graph.add_edge("C", "D")
    my_undirected_graph.add_edge("G", "A")

    undirected_graph_a_c_path: Union[List, None] = my_undirected_graph.find_path("A", "C")
    undirected_graph_a_g_path: Union[List, None] = my_undirected_graph.find_path("A", "G")
    undirected_has_cycles: bool = my_undirected_graph.is_cyclic()

    test = 'test'


if __name__ == '__main__':
    main()
