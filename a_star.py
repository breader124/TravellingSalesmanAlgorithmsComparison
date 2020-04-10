from time import process_time
import heapq

from misc import dist
from heuristic_algorithm import HeuristicAlgorithm


class AStarAlgorithm(HeuristicAlgorithm):
    def __init__(self, nodes):
        HeuristicAlgorithm.__init__(self, nodes)
        self.states = []

    def run(self):
        time_start = process_time()

        heapq.heappush(self.states, (0, self.current_state))

        while not self.is_terminal_state():
            self.update_expanded_state()
            self.update_states_vector()
            self.update_current_state()

        path = self.current_state
        cost = self.dist_from_beginning(path)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def update_states_vector(self):
        dist_to_state, _ = heapq.heappop(self.states)
        for s in self.expanded_state:
            if self.chose_home_too_early(s):
                dist_from_beg = float('inf')
            else:
                dist_from_beg = dist_to_state + dist(s[-2], s[-1])
            cost = dist_from_beg + self.heuristic.compute(s)
            heapq.heappush(self.states, (cost, s))

    def update_current_state(self):
        popped = heapq.heappop(self.states)
        self.current_state = popped[1]
        heapq.heappush(self.states, popped)
