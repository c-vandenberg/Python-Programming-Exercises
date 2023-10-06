#!/usr/bin/env python3

from data_structures.exercise_47.stacks import Stack
from graphs import DirectedGraph, UndirectedGraph
from typing import Any, Union, List, Set


def main():
    # Create directed graph
    dfs_stack = Stack()
    my_directed_graph = DirectedGraph(dfs_stack)

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

    directed_has_cycles: bool = my_directed_graph.is_cyclic()

    # Create undirected graph
    dfs_stack = Stack()
    my_undirected_graph = UndirectedGraph(dfs_stack)

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
    my_undirected_graph.add_edge("C", "G")
    my_undirected_graph.add_edge("G", "A")


    undirected_has_cycles: bool = my_undirected_graph.is_cyclic()

    test = 'test'


if __name__ == '__main__':
    main()
