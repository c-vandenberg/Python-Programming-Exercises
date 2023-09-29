#!/usr/bin/env python3

from typing import Any, Union


class BaseGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node: Any):
        if node not in self.nodes:
            # Nodes are defined as dictionary key with the edges being a list of neighbouring nodes
            self.nodes[node] = []

    def add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None] = None):
        self._add_edge(from_node, to_node, weight)

    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        # Add edge logic to be implemented in child class
        pass

    def __str__(self):
        return str(self.nodes)


class DirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node] = [
                {(from_node, to_node): weight}
            ]


class UndirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node] = [
                {(from_node, to_node): weight}
            ]
            self.nodes[to_node] = [
                {(to_node, from_node): weight}
            ]
