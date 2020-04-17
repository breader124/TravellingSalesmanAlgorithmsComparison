from time import process_time
import heapq

from misc import dist, Edge


class AStarAlgorithm:
    def __init__(self, nodes):
        self.nodes = nodes
        self.states = []
        heapq.heapify(self.states)

    def run(self):
        edges = self.edges_from_nodes(self.nodes)
        edges.sort(key=self.take_len)

        time_start = process_time()

        current_state = [self.nodes[0]]
        states = []

        # cost, heuristic, current_state
        heapq.heappush(states, (0, 0, current_state))

        while not self.is_terminal_state(current_state, self.nodes):
            nodes_left = self.get_nodes_left(self.nodes, current_state)
            current_expanded = self.get_expanded_state(current_state,
                                                       nodes_left)
            states = self.get_updated_states_vector(edges, states,
                                                    current_expanded,
                                                    self.nodes, nodes_left)
            current_state = self.get_current_state(states)

        path, cost = current_state, self.dist_from_beginning(current_state,
                                                             self.nodes[0],
                                                             len(self.nodes))

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def is_terminal_state(self, current_state, nodes):
        return len(set(current_state)) == len(nodes) and current_state[-1] == \
               nodes[0]

    def get_nodes_left(self, nodes, current_state):
        nodes_left = set(nodes).difference(current_state)
        nodes_left = list(nodes_left)
        nodes_left.append(nodes[0])

        return nodes_left

    def get_expanded_state(self, current_state, nodes_left):
        expanded = []

        for node in nodes_left:
            expanded.append([*current_state, node])

        return expanded

    def get_current_state(self, states):
        popped = heapq.heappop(states)
        current_state = popped[2]
        heapq.heappush(states, popped)

        return current_state

    def get_updated_states_vector(self, edges, states, expanded, nodes,
                                  nodes_left):
        d, h, _ = heapq.heappop(states)
        without_heuristic = d - h
        for s in expanded:
            if self.chose_home_too_early(s, nodes[0], len(nodes) + 1):
                continue
            else:
                dist_from_beg = without_heuristic + dist(s[-2], s[-1])

            heur = self.heuristic(edges, s, nodes, nodes_left)
            cost = dist_from_beg + heur
            heapq.heappush(states, (cost, heur, s))

        return states

    def dist_from_beginning(self, state, start_node, total_size):
        if self.chose_home_too_early(state, start_node, total_size):
            return float('inf')

        d = 0
        for i in range(1, len(state)):
            d = d + dist(state[i - 1], state[i])

        return d

    def chose_home_too_early(self, state, start_node, total_size):
        return len(state) < total_size and state[-1] == start_node

    def heuristic(self, edges, state, nodes, nodes_left):
        span_tree = True
        if span_tree:
            return self.kruskal_algorithm(nodes_left, edges, state)
        else:
            nodes_left = len(nodes) - len(state) + 1
            return self.min_edge_len_between_not_used_nodes(edges,
                                                            state) * nodes_left

    def kruskal_algorithm(self, nodes_left, all_edges, state):
        msp_tree_dist = 0
        nodes_left = set(nodes_left) - set(state)

        if not nodes_left:
            return 0

        edges = self.edges_from_nodes(nodes_left)

        edges.sort(key=self.take_len)

        same_nodes = set()
        while edges and len(same_nodes) < len(nodes_left):
            current_edge = edges[0]
            if current_edge.first_node not in same_nodes or current_edge.second_node not in same_nodes:
                same_nodes.add(current_edge.first_node)
                same_nodes.add(current_edge.second_node)
                msp_tree_dist = msp_tree_dist + current_edge.length

            edges.remove(current_edge)

        start_node = state[0]
        start_len = float('inf')
        start_found = False

        end_node = state[-1]
        end_len = float('inf')
        end_found = False
        for e in all_edges:
            if not start_found and ((
                    e.first_node == start_node and e.second_node in nodes_left) or (
                    e.first_node in nodes_left and e.second_node == start_node)):
                start_len = e.length
                start_found = True
            if not end_found and ((
                    e.first_node == end_node and e.second_node in nodes_left) or (
                    e.first_node in nodes_left and e.second_node == end_node)):
                end_len = e.length
                end_found = True
            if start_found and end_found:
                break

        return start_len + msp_tree_dist + end_len

    def edges_from_nodes(self, nodes):
        nodes = list(nodes)
        second = nodes.copy()
        second.reverse()
        edges = []

        for first_node in nodes:
            second.pop()
            for second_node in second:
                edge_len = dist(first_node, second_node)
                edges.append(Edge(first_node, second_node, edge_len))

        return edges

    def min_edge_len_between_not_used_nodes(self, edges, state):
        for edge in edges:
            if not self.edge_used(edge, state):
                return edge.length
        return 0.0

    def one_node_from_path_left(self, state, nodes):
        return len(state) == len(nodes) - 1

    def full_path_done(self, state, nodes):
        return len(state) == len(nodes)

    def at_the_beginning(self, state, nodes):
        return len(state) == len(nodes) + 1

    def edge_used(self, edge, state):
        try:
            first = state.index(edge.first_node.label)
            second = state.index(edge.first_node.label)
            return abs(first - second) == 1
        except ValueError:
            return False

    def take_len(self, edge):
        return edge.length
