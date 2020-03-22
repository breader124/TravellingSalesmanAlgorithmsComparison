from time import process_time
import heapq

from misc import edges_from_nodes, take_len
from algorithm import Algorithm
from heuristics import heuristic


class AStarAlgorithm(Algorithm):
    def __init__(self, nodes):
        Algorithm.__init__(self, nodes)
        self.states = []

    def run(self):
        edges = edges_from_nodes(self.nodes)
        edges.sort(key=take_len)

        time_start = process_time()

        heapq.heappush(self.states, (0, self.current_state))

        while not self.is_terminal_state():
            self.update_expanded_state()
            self.update_states_vector(edges)
            self.update_current_state()

        path, cost = self.current_state, self.dist_from_beginning(self.current_state)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def update_states_vector(self, edges):
        heapq.heappop(self.states)
        for s in self.expanded_state:
            dist_from_beg = self.dist_from_beginning(s)
            cost = dist_from_beg + heuristic(edges, s, self.nodes)
            heapq.heappush(self.states, (cost, s))

    def update_current_state(self):
        popped = heapq.heappop(self.states)
        self.current_state = popped[1]
        heapq.heappush(self.states, popped)
