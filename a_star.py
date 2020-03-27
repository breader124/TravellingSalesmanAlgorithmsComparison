from time import process_time
import heapq

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
        heapq.heappop(self.states)
        for s in self.expanded_state:
            dist_from_beg = self.dist_from_beginning(s)
            cost = dist_from_beg + self.heuristic.compute(s)
            heapq.heappush(self.states, (cost, s))

    def update_current_state(self):
        popped = heapq.heappop(self.states)
        self.current_state = popped[1]
        heapq.heappush(self.states, popped)
