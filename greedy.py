from time import process_time

from heuristic_algorithm import HeuristicAlgorithm


class GreedyAlgorithm(HeuristicAlgorithm):
    def __init__(self, nodes):
        HeuristicAlgorithm.__init__(self, nodes)

    def run(self):
        time_start = process_time()

        while not self.is_terminal_state():
            self.update_expanded_state()
            self.update_current_state()

        path, cost = self.current_state, self.dist_from_beginning(self.current_state)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def update_current_state(self):
        min_cost = float('inf')
        cheapest_state = []

        for s in self.expanded_state:
            dist_from_beg = self.dist_from_beginning(s)
            cost = dist_from_beg + self.heuristic.compute(s)
            if cost < min_cost:
                min_cost = cost
                cheapest_state = s

        self.current_state = cheapest_state
