from time import process_time
from misc import dist
from algorithm import Algorithm


class BruteForce(Algorithm):
    def __init__(self, nodes):
        Algorithm.__init__(self, nodes)

    def run(self):
        time_start = process_time()

        first_node = self.nodes[0]
        path, cost = self._recurrent(first_node, first_node, self.nodes[1:])
        path = [first_node] + path

        time_end = process_time()
        time_elapsed = time_end - time_start

        return path, cost, time_elapsed

    def _recurrent(self, first_node, current_node, nodes_left):
        if len(nodes_left) == 0:
            return [first_node], dist(current_node, first_node)

        best_path = []
        best_cost = float('inf')

        for node in nodes_left:
            subset = nodes_left.copy()
            subset.remove(node)
            subpath, subcost = self._recurrent(first_node, node, subset)
            subcost += dist(current_node, node)

            if subcost < best_cost:
                best_cost = subcost
                best_path = [node] + subpath

        return best_path, best_cost
