#!/usr/bin/env python3

from graphs import DirectedGraph


def main():
    # Create a graph
    my_graph = DirectedGraph()

    # Add nodes
    my_graph.add_node("A")
    my_graph.add_node("B")
    my_graph.add_node("C")

    # Add edges
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")

    print(my_graph)


if __name__ == '__main__':
    main()
