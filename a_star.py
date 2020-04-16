from time import process_time
import heapq

from heuristic_algorithm import HeuristicAlgorithm
from misc import dist


class AStarAlgorithm(HeuristicAlgorithm):
    def __init__(self, nodes):
        HeuristicAlgorithm.__init__(self, nodes)
        self.states = []
        heapq.heapify(self.states)

    def run(self):
        time_start = process_time()

        current_state = [self.nodes[0]]
        current_cost = 0
        nodes_left = self.nodes[1:]
        nodes_set = set(self.nodes)

        while len(current_state) != len(self.nodes) + 1:
            nodes_left = [
                node
                for node in self.nodes
                if node not in current_state
            ]

            if len(nodes_left) == 0:
                considered = current_state + [self.nodes[0]]
                cost = dist(current_state[-1], self.nodes[0])
                new_cost = current_cost + cost
                heapq.heappush(self.states, (new_cost, (new_cost, considered)))

            for node in nodes_left:
                considered = current_state + [node]
                cost = dist(current_state[-1], node)
                estimated_remaining = self.heuristic.compute(considered, 'mst')
                new_cost = current_cost + cost
                heapq.heappush(self.states, (new_cost + estimated_remaining, (new_cost, considered)))
            _, (current_cost, current_state) = heapq.heappop(self.states)

        path = current_state
        cost = self.dist_from_beginning(path)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed
