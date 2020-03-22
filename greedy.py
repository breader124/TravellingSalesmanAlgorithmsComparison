from time import process_time

from misc import *
from algorithm import Algorithm
from heuristics import heuristic


class GreedyAlgorithm(Algorithm):
    def __init__(self, nodes):
        Algorithm.__init__(self, nodes)

    def run(self):
        edges = edges_from_nodes(self.nodes)
        edges.sort(key=take_len)

        time_start = process_time()

        while not self.is_terminal_state():
            self.update_expanded_state()
            self.update_current_state(edges)

        path, cost = self.current_state, self.dist_from_beginning(self.current_state)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def update_current_state(self, edges):
        min_cost = float('inf')
        cheapest_state = []

        for s in self.expanded_state:
            dist_from_beg = self.dist_from_beginning(s)
            cost = dist_from_beg + heuristic(edges, s, self.nodes)
            if cost < min_cost:
                min_cost = cost
                cheapest_state = s

        self.current_state = cheapest_state
