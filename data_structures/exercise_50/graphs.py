#!/usr/bin/env python3

from typing import Any, Union, List, Set
from data_structures.exercise_47.stacks import Stack


class BaseGraph:
    def __init__(self, dfs_stack: Stack):
        self.dfs_stack = dfs_stack
        self._nodes = {}
        self._visited_nodes = set()
        self._traversal_order = []

    def add_node(self, node: Any):
        if node not in self._nodes:
            # Nodes are defined as dictionary key with the edges being a list of neighbouring nodes
            self._nodes[node] = []

    def add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None] = None):
        self._add_edge(from_node, to_node, weight)

    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        # Add edge logic to be implemented in child class
        pass

    def _validate_nodes(self, start_node: Any, end_node: Union[None, Any] = None):
        if start_node not in self._nodes or (end_node not in self._nodes and end_node):
            missing_node: Any = start_node if start_node not in self._nodes else end_node
            raise ValueError(f'Node {missing_node} not present in Graph')

    def dfs_find_path(self, start_node: Any, end_node: Union[None, Any] = None) -> Union[List, None]:
        self._validate_nodes(start_node, end_node)

        self.dfs_stack.push_top(start_node)
        self._traversal_order.append(start_node)
        self._visited_nodes.add(start_node)

        while self.dfs_stack:
            current_node = self.dfs_stack.pop_top()

            if current_node == end_node:
                self._traversal_order.append(current_node)
                path: List = self._traversal_order
                self._visited_nodes.clear()
                self.dfs_stack.clear_stack()
                return path

            if current_node not in self._visited_nodes:
                self._traversal_order.append(current_node)
                self._visited_nodes.add(current_node)

            # Push unvisited current_node neighbours onto the stack
            for neighbour in self._nodes[current_node]:
                edge: tuple = list(neighbour.keys())[0]
                for neighbour_node in edge:
                    if neighbour_node not in self._visited_nodes:
                        self.dfs_stack.push_top(neighbour_node)

        self._visited_nodes.clear()
        self.dfs_stack.clear_stack()
        return None

    def _dfs(self, start_node: Any):
        self._validate_nodes(start_node)

        connected_nodes: Set = set()
        self.dfs_stack.push_top(start_node)

        while self.dfs_stack:
            current_node = self.dfs_stack.pop_top()

            if current_node not in self._visited_nodes:
                self._visited_nodes.add(current_node)
                connected_nodes.add(current_node)

                # Push unvisited current_node neighbours onto the stack
                for neighbour in self._nodes[current_node]:
                    edge: tuple = list(neighbour.keys())[0]
                    for neighbour_node in edge:
                        if neighbour_node not in self._visited_nodes:
                            self.dfs_stack.push_top(neighbour_node)

        return connected_nodes

    def connected_components(self) -> list:
        connected_components_list = []
        for node in self._nodes:
            connected_nodes = self._dfs(node)
            connected_components_list.append(connected_nodes)

        self._visited_nodes.clear()
        self.dfs_stack.clear_stack()
        return connected_components_list

    def __str__(self):
        return str(self._nodes)


class DirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self._nodes and to_node in self._nodes:
            self._nodes[from_node].append(
                {(from_node, to_node): weight}
            )


class UndirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self._nodes and to_node in self._nodes:
            self._nodes[from_node].append(
                {(from_node, to_node): weight}
            )
            self._nodes[to_node].append(
                {(to_node, from_node): weight}
            )
