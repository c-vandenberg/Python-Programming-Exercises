#!/usr/bin/env python3

from data_structures.exercise_46.queues import GenericFifoQueue
from collections import defaultdict
from typing import Any, Union, List, Set, Dict, Tuple
from helpers.exception_helpers import CycleError


class BaseGraph:
    def __init__(self, bfs_queue: GenericFifoQueue):
        self._bfs_queue = bfs_queue
        self._nodes = defaultdict(list)
        self._visited_nodes = set()
        self._traversal_order = []
        self._has_path = False

    def add_node(self, node: Any):
        if node not in self._nodes:
            # Nodes are defined as dictionary key with the edges being a list of neighbouring nodes
            self._nodes[node] = []

    def add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None] = None):
        self._add_edge(from_node, to_node, weight)

    def _add_edge(self, from_node: Any, to_node: Any, weight: Union[int, float, None]):
        # Add edge logic to be implemented in child class
        pass

    """ Nodes getter """
    @property
    def nodes(self) -> Dict[Union[int, float], List[Dict]]:
        return self._nodes

    """ Validate nodes passed to class methods """
    def _validate_nodes(self, start_node: Any, end_node: Union[None, Any] = None):
        if start_node not in self._nodes or (end_node not in self._nodes and end_node):
            missing_node: Any = start_node if start_node not in self._nodes else end_node

            raise ValueError(f'Node {missing_node} not present in Graph')

    """ Depth-First Search (DFS) algorithm to traverse graph """
    def _dfs(self, node: Any, end_node: Union[None, Any] = None) -> None:
        self._visited_nodes.add(node)
        self._traversal_order.append(node)

        if node == end_node:
            self._has_path = True
            return

        for edge in self._nodes[node]:
            neighbour_node: Any = list(edge.keys())[0]
            if neighbour_node not in self._visited_nodes:
                self._dfs(neighbour_node, end_node)

    """ Breadth-First Search (BFS) algorithm to traverse graph """
    def _bfs(self, start_node: Any, end_node: Union[None, Any] = None) -> None:
        if len(self._visited_nodes) != 0:
            self._visited_nodes.clear()

        if len(self._traversal_order) != 0:
            self._traversal_order.clear()

        self._bfs_queue.enqueue(start_node)
        self._visited_nodes.add(start_node)
        self._traversal_order.append(start_node)

        while self._bfs_queue:
            current_node = self._bfs_queue.dequeue()

            if current_node == end_node:
                self._has_path = True
                return

            for edge in self._nodes[current_node]:
                neighbour_node: Any = list(edge.keys())[0]
                if neighbour_node not in self._visited_nodes:
                    self._bfs_queue.enqueue(neighbour_node)
                    self._visited_nodes.add(neighbour_node)
                    self._traversal_order.append(neighbour_node)

    """ Use DFS algorithm to find path between two nodes (N.B. will not necessarily be the shortest path) """
    def find_path(self, start_node: Any, end_node: Union[None, Any] = None) -> Union[List, None]:
        self._validate_nodes(start_node, end_node)
        path: Union[List, None] = None
        self._dfs(start_node, end_node)

        if self._has_path:
            path = self._traversal_order[:]
            self._has_path = False

        self._visited_nodes.clear()
        self._traversal_order.clear()

        return path

    """ Use BFS algorithm to find the shortest find path between two nodes """
    def find_shortest_path(self, start_node: Any, end_node: Union[None, Any] = None) -> Union[List, None]:
        self._validate_nodes(start_node, end_node)
        path: Union[List, None] = None
        self._bfs(start_node, end_node)

        if self._has_path:
            path = self._traversal_order[:]
            self._has_path = False

        self._visited_nodes.clear()
        self._traversal_order.clear()

        return path

    """ Return all connected components in graph (i.e. all nodes that have neighbours) """
    def connected_components(self) -> Set:
        for node in self._nodes:
            if self._has_traversable_neighbours(self._nodes[node]) and node not in self._visited_nodes:
                self._dfs(node)

        connected_components: Set = set(self._visited_nodes)
        self._visited_nodes.clear()
        self._traversal_order.clear()

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
        for edge in self._nodes[current_node]:
            neighbour_node_tuple: Tuple = list(edge.items())[0]
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

    def topological_sort(self) -> List[Any]:
        # A cyclic graph cannot have valid topological sorting. Raise error if graph contains cycles
        if self.is_cyclic():
            raise CycleError('A cyclic graph cannot have valid topological sorting')

        # Mark all nodes as not visited and initialise stack that will be used to store the topologically sorted nodes
        visited: Dict = {node: False for node in self._nodes}
        stack: List = []

        # Call recursive helper function to store nodes in topological sorted list
        for node in visited:
            # Only call recursive helper function on nodes we haven't yet visited
            if not visited[node]:
                self._topological_sort_util(node, visited, stack)

        return stack

    def _topological_sort_util(self, current_node: Any, visited: Dict[Any, bool], stack: List):
        # Mark current node as visited
        visited[current_node] = True

        # Recursively visit all nodes along the branch from the current node
        for edge in self._nodes[current_node]:
            neighbour_node_tuple: Tuple = list(edge.items())[0]
            neighbour_node: Any = neighbour_node_tuple[0]

            if not visited[neighbour_node]:
                self._topological_sort_util(neighbour_node, visited, stack)

        stack.insert(0, current_node)


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
        for edge in self._nodes[current_node]:
            neighbour_node_tuple: Tuple = list(edge.items())[0]
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
