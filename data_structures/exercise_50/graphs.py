#!/usr/bin/env python3

from collections import defaultdict
from typing import Any, Union, List, Set, Dict, Tuple
from data_structures.exercise_47.stacks import Stack


class BaseGraph:
    def __init__(self, dfs_stack: Stack):
        self._dfs_stack = dfs_stack
        self._nodes = defaultdict(list)
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

    """ Validate nodes passed to class methods """
    def _validate_nodes(self, start_node: Any, end_node: Union[None, Any] = None):
        if start_node not in self._nodes or (end_node not in self._nodes and end_node):
            missing_node: Any = start_node if start_node not in self._nodes else end_node

            raise ValueError(f'Node {missing_node} not present in Graph')

    """ Depth First Search (DFS) algorithm to traverse graph """
    def _dfs(self, node: Any, end_node: Union[None, Any] = None, detect_cycle: bool = False):
        self._visited_nodes.add(node)
        self._traversal_order.append(node)

        if node == end_node:
            self._traversal_order.append(node)
            return

        for neighbour in self._nodes[node]:
            edge: tuple = list(neighbour.keys())[0]
            neighbour_node = edge[1] if edge[0] == node else edge[0]
            if neighbour_node not in self._visited_nodes:
                self._dfs(neighbour_node, end_node)

    """ Use DFS algorithm to find path between two nodes (N.B. will not necessarily be the shortest path"""
    def find_path(self, start_node: Any, end_node: Union[None, Any] = None) -> Union[List, None]:
        self._validate_nodes(start_node, end_node)
        self._dfs(start_node, end_node)

        path: Union[List, None] = self._traversal_order[:]
        self._visited_nodes.clear()
        self._traversal_order.clear()
        self._dfs_stack.clear_stack()

        return path

    """ Return all connected components in graph (i.e. all nodes that have neighbours """
    def connected_components(self) -> Set:
        for node in self._nodes:
            if self._has_traversable_neighbours(self._nodes[node]) and node not in self._visited_nodes:
                self._dfs(node)

        connected_components: Set = set(self._visited_nodes)
        self._visited_nodes.clear()
        self._traversal_order.clear()
        self._dfs_stack.clear_stack()

        return connected_components

    @staticmethod
    def _has_traversable_neighbours(node: Any) -> bool:
        return True if len(node) != 0 else False

    def __str__(self):
        return str(self._nodes)


class DirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        if from_node in self._nodes and to_node in self._nodes:
            self._nodes[from_node].append(
                {to_node: weight}
            )

    """ Determines if graph is cyclic or not """
    def is_cyclic(self):
        # Mark all nodes as not visited and initialise recursion stack for all nodes
        visited: Dict = {node: False for node in self._nodes}
        recursion_stack = {node: False for node in self._nodes}

        # Call recursive helper function to detect cycles in graph
        for node in visited:
            # Only attempt cycle detection on nodes we haven't visited yet
            if not visited[node]:
                if self._detect_cycles(node, visited, recursion_stack):
                    return True

        return False

    """ Recursive function to detect cycle in subgraph """
    def _detect_cycles(self, current_node: Any, visited: Dict[Any, bool], recursion_stack: Union[Dict, bool]):
        # Mark current node as visited and add to recursion stack
        visited[current_node] = True
        recursion_stack[current_node] = True

        # Recursively visit all nodes along the branch from the current node
        for neighbour_node_dict in self._nodes[current_node]:
            neighbour_node_tuple: Tuple = list(neighbour_node_dict.items())[0]
            neighbour_node: Any = neighbour_node_tuple[0]

            # If the neighbouring node has not yet been visited, recursively visit its neighbouring nodes
            if not visited[neighbour_node]:
                if self._detect_cycles(neighbour_node, visited, recursion_stack):
                    return True

            # If current neighbour is in recursive stack then we have already visited it in this branch search and so
            # there must be a cycle in the graph
            elif recursion_stack[neighbour_node]:
                return True

        recursion_stack[current_node] = False
        return False


class UndirectedGraph(BaseGraph):
    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        self._validate_nodes(from_node, to_node)
        self._nodes[from_node].append(
            {to_node: weight}
        )
        self._nodes[to_node].append(
            {from_node: weight}
        )

    """ Determines if graph is cyclic or not """
    def is_cyclic(self):
        # Mark all nodes as not visited
        visited: Dict = {node: False for node in self._nodes}

        # Call recursive helper function to detect cycles in Graph
        for node in visited:
            # Only detect cycles if we haven't yet visited it
            if not visited[node]:
                if self._detect_cycles(node, visited):
                    return True

        return False

    """ Recursive function to detect cycle in subgraph """
    def _detect_cycles(self, current_node: Any, visited: Dict[Any, bool], parent_node: Any = None,):

        # Mark current node as visited and mark recursion stack as visited if we have a directed graph
        visited[current_node] = True

        # Recursively visit all nodes along the branch from the current node
        for neighbour_node_dict in self._nodes[current_node]:
            neighbour_node_tuple: Tuple = list(neighbour_node_dict.items())[0]
            neighbour_node: Any = neighbour_node_tuple[0]

            # If the neighbouring node has not yet been visited, recursively visit its neighbouring nodes
            if not visited[neighbour_node]:
                if self._detect_cycles(neighbour_node, visited, current_node):
                    return True

            # If the current neighbour has been visited and is not the parent node/root node from this branch search,
            # there must be a cycle in the graph
            elif parent_node != neighbour_node:
                return True

        return False
