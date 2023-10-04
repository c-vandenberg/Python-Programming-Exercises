#!/usr/bin/env python3

from data_structures.exercise_47.stacks import Stack
from graphs import DirectedGraph
from typing import Any, Union, List


def main():
    # Create a graph
    dfs_stack = Stack()
    my_graph = DirectedGraph(dfs_stack)

    # Add nodes
    my_graph.add_node("A")
    my_graph.add_node("B")
    my_graph.add_node("C")
    my_graph.add_node("D")
    my_graph.add_node("E")
    my_graph.add_node("F")
    my_graph.add_node("G")
    my_graph.add_node("H")
    my_graph.add_node("I")

    # Add edges
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("B", "D")
    my_graph.add_edge("B", "E")
    my_graph.add_edge("B", "F")
    my_graph.add_edge("F", "G")
    my_graph.add_edge("G", "H")
    my_graph.add_edge("G", "I")

    visited_nodes: Union[List, None] = my_graph.dfs_find_path("B", "H")

    test = 'test'


if __name__ == '__main__':
    main()
