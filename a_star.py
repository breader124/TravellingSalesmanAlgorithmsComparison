from time import process_time
import heapq

from misc import dist, edges_from_nodes


def take_len(edge):
    return edge.length


def dist_from_beginning(state):
    d = 0
    for i in range(1, len(state)):
        d = d + dist(state[i - 1], state[i])

    return d


def is_connected_with_mst(edge, node, nodes_left):
    first_connected = edge.first_node == node and edge.second_node in nodes_left
    second_connected = edge.first_node in nodes_left and edge.second_node == node
    return first_connected or second_connected


class AStarAlgorithm:
    def __init__(self, nodes):
        self.nodes = nodes
        self.states = []
        self.current_state = [self.nodes[0]]

        self.edges = edges_from_nodes(self.nodes)
        self.edges.sort(key=take_len)

        heapq.heapify(self.states)

    def run(self):

        time_start = process_time()

        # cost, heuristic, current_state
        heapq.heappush(self.states, (0, 0, self.current_state))

        while not self.is_terminal_state():
            nodes_left = self.get_nodes_left()
            current_expanded = self.get_expanded_state(nodes_left)
            self.update_states_vector(current_expanded, nodes_left)
            self.update_current_state()

        path, cost = self.current_state, dist_from_beginning(self.current_state)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def is_terminal_state(self):
        all_included = len(set(self.current_state)) == len(self.nodes)
        first_node_repeated = self.current_state[-1] == self.nodes[0]

        return all_included and first_node_repeated

    def get_nodes_left(self):
        nodes_left = set(self.nodes).difference(self.current_state)
        nodes_left = list(nodes_left)
        nodes_left.append(self.nodes[0])

        return nodes_left

    def get_expanded_state(self, nodes_left):
        expanded = []
        for node in nodes_left:
            expanded.append([*self.current_state, node])

        return expanded

    def update_current_state(self):
        popped = heapq.heappop(self.states)
        self.current_state = popped[2]
        heapq.heappush(self.states, popped)

    def update_states_vector(self, expanded, nodes_left):
        d, h, _ = heapq.heappop(self.states)
        without_heuristic = d - h
        for s in expanded:
            if self.chose_home_too_early(s):
                continue
            else:
                dist_from_beg = without_heuristic + dist(s[-2], s[-1])

            heur = self.heuristic(s, nodes_left)
            cost = dist_from_beg + heur
            heapq.heappush(self.states, (cost, heur, s))

    def chose_home_too_early(self, state):
        total_size = len(self.nodes) + 1
        return len(state) < total_size and state[0] == state[-1]

    def heuristic(self, state, nodes_left):
        return self.kruskal_algorithm(state, nodes_left)

    def kruskal_algorithm(self, state, nodes_left):
        msp_tree_dist = 0
        nodes_left = set(nodes_left) - set(state)

        if not nodes_left:
            return 0

        edges = edges_from_nodes(nodes_left)
        edges.sort(key=take_len)

        same_nodes = set()
        while edges and len(same_nodes) < len(nodes_left):
            current_edge = edges[0]
            if current_edge.first_node not in same_nodes or current_edge.second_node not in same_nodes:
                same_nodes.add(current_edge.first_node)
                same_nodes.add(current_edge.second_node)
                msp_tree_dist = msp_tree_dist + current_edge.length

            edges.remove(current_edge)

        start_len, end_len = self.dist_to_mst(state, nodes_left)

        return start_len + msp_tree_dist + end_len

    def dist_to_mst(self, state, nodes_left):
        start_node = state[0]
        start_len = float('inf')
        start_found = False

        end_node = state[-1]
        end_len = float('inf')
        end_found = False

        for e in self.edges:
            if not start_found and is_connected_with_mst(e, start_node, nodes_left):
                start_len = e.length
                start_found = True
            if not end_found and is_connected_with_mst(e, end_node, nodes_left):
                end_len = e.length
                end_found = True
            if start_found and end_found:
                break

        return start_len, end_len
