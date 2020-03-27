from time import process_time

from heuristic_algorithm import HeuristicAlgorithm
from misc import dist


class GreedyAlgorithm(HeuristicAlgorithm):
    def __init__(self, nodes):
        HeuristicAlgorithm.__init__(self, nodes)

    def run(self):
        time_start = process_time()

        nodes_left = self.nodes[1:]
        path = [self.nodes[0]]

        while len(nodes_left) > 0:
            min_cost = float('inf')
            min_node = 0
            for node in nodes_left:
                cost = dist(path[-1], node)
                estimated_remaining = self.heuristic.compute(path + [node])

                if cost + estimated_remaining < min_cost:
                    min_cost = cost + estimated_remaining
                    min_node = node

            path.append(min_node)
            nodes_left.remove(min_node)
        path.append(self.nodes[0])

        cost = self.dist_from_beginning(path)

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed
