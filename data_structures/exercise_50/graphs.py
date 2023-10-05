#!/usr/bin/env python3

from typing import Any, Union, List, Set
from data_structures.exercise_47.stacks import Stack


class BaseGraph:
    def __init__(self, dfs_stack: Stack):
        self._dfs_stack = dfs_stack
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

    @staticmethod
    def _has_traversable_neighbours(node: Any) -> bool:
        return True if len(node) != 0 else False

    def find_path(self, start_node: Any, end_node: Union[None, Any] = None) -> Union[List, None]:
        self._dfs_directed(start_node, end_node)

        path: Union[List, None] = self._traversal_order[:]
        self._visited_nodes.clear()
        self._traversal_order.clear()
        self._dfs_stack.clear_stack()

        return path

    def connected_components(self) -> Set:
        for node in self._nodes:
            if self._has_traversable_neighbours(self._nodes[node]) and node not in self._visited_nodes:
                self._dfs_directed(node)

        connected_components: Set = set(self._visited_nodes)
        self._visited_nodes.clear()
        self._traversal_order.clear()
        self._dfs_stack.clear_stack()

        return connected_components

    def has_cycles(self, start_node: Any):
        # Has cycles logic to be implemented in child class
        pass

    def _detect_cycles(self, current_node: Any, parent_node: Any = None):
        # Detect cycles logic to be implemented in child class
        pass



    def _dfs_directed(self, start_node: Any, end_node: Union[None, Any] = None, detect_cycle: bool = False) \
            -> Union[None, bool]:
        self._dfs_stack.push_top(start_node)
        self._traversal_order.append(start_node)
        self._visited_nodes.add(start_node)

        while self._dfs_stack:
            current_node = self._dfs_stack.pop_top()

            if current_node == end_node:
                self._traversal_order.append(current_node)
                return

            if current_node not in self._visited_nodes:
                self._traversal_order.append(current_node)
                self._visited_nodes.add(current_node)

            # Push unvisited current_node neighbours onto the stack
            for neighbour in self._nodes[current_node]:
                edge: tuple = list(neighbour.keys())[0]
                for neighbour_node in edge:
                    if neighbour_node == current_node:
                        continue
                    elif detect_cycle and neighbour_node in self._traversal_order:
                        if self._detect_cycles(neighbour_node, current_node):
                            return True
                    elif neighbour_node not in self._visited_nodes:
                        self._dfs_stack.push_top(neighbour_node)

    def _dfs_undirected(self, start_node: Any, end_node: Union[None, Any] = None, detect_cycle: bool = False) \
            -> Union[None, bool]:
        self._validate_nodes(start_node, end_node)

        self._dfs_stack.push_top(start_node)
        self._visited_nodes.add(start_node)

        while self._dfs_stack:
            current_node = self._dfs_stack.pop_top()

            if current_node == end_node:
                self._traversal_order.append(current_node)
                return

            self._traversal_order.append(current_node)

            # Push unvisited current_node neighbours onto the stack
            for neighbour in self._nodes[current_node]:
                edge: tuple = list(neighbour.keys())[0]
                neighbour_node = edge[1] if edge[0] == current_node else edge[0]

                if detect_cycle and neighbour_node in self._traversal_order:
                    if self._detect_cycles(neighbour_node, current_node):
                        return True

                if neighbour_node in self._visited_nodes:
                    continue

                self._dfs_stack.push_top(neighbour_node)
                self._visited_nodes.add(neighbour_node)

    def _validate_nodes(self, start_node: Any, end_node: Union[None, Any] = None):
        if start_node not in self._nodes or (end_node not in self._nodes and end_node):
            missing_node: Any = start_node if start_node not in self._nodes else end_node
            raise ValueError(f'Node {missing_node} not present in Graph')

    def __str__(self):
        return str(self._nodes)


class DirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self._nodes and to_node in self._nodes:
            self._nodes[from_node].append(
                {(from_node, to_node): weight}
            )

    def has_cycles(self, start_node: Any):
        return True if self._dfs_undirected(start_node, detect_cycle=True) else False

    def _detect_cycles(self, current_node: Any, parent_node: Any = None):
        return True if current_node in self._traversal_order else False


class UndirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self._nodes and to_node in self._nodes:
            self._nodes[from_node].append(
                {(from_node, to_node): weight}
            )
            self._nodes[to_node].append(
                {(to_node, from_node): weight}
            )

    def has_cycles(self, start_node: Any):
        return True if self._dfs_undirected(start_node, detect_cycle=True) else False

    def _detect_cycles(self, current_node: Any, parent_node: Any = None):
        for neighbour in self._nodes[current_node]:
            edge: tuple = list(neighbour.keys())[0]
            for neighbour_node in edge:
                if neighbour_node == current_node:
                    continue
                elif neighbour_node == parent_node:
                    return True if current_node in self._traversal_order and neighbour_node != parent_node else False
