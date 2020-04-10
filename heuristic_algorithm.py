from misc import dist
from heuristics import Heuristic
from algorithm import Algorithm


class HeuristicAlgorithm(Algorithm):
    def __init__(self, nodes):
        Algorithm.__init__(self, nodes)
        self.nodes_left = []
        self.current_state = [self.nodes[0]]
        self.expanded_state = []
        self.heuristic = Heuristic(nodes)

    def is_terminal_state(self):
        return self.is_all_nodes_included() and self.is_last_node_is_start_node()

    def is_all_nodes_included(self):
        return len(set(self.current_state)) == len(self.nodes)

    def is_last_node_is_start_node(self):
        return self.current_state[-1] == self.nodes[0]

    def update_expanded_state(self):
        self.update_nodes_left()
        self.expanded_state = []

        for node in self.nodes_left:
            self.expanded_state.append([*self.current_state, node])

    def update_nodes_left(self):
        self.nodes_left = list(set(self.nodes).difference(self.current_state))
        self.nodes_left.append(self.nodes[0])

    def dist_from_beginning(self, state_to_measure):
        if self.chose_home_too_early(state_to_measure):
            return float('inf')

        total_dist = 0
        for i in range(1, len(state_to_measure)):
            previous_node = state_to_measure[i - 1]
            current_node = state_to_measure[i]
            total_dist = total_dist + dist(previous_node, current_node)

        return total_dist

    def chose_home_too_early(self, state_to_measure):
        not_full_cycle = len(state_to_measure) < (len(self.nodes) + 1)
        start_node_chosen = state_to_measure[-1] == self.nodes[0]
        return not_full_cycle and start_node_chosen
