from time import process_time
from misc import dist


def brute_force(nodes):
    time_start = process_time()

    path, cost = _recurrent(nodes[0], nodes[1:])
    path = [nodes[0]] + path + [nodes[0]]

    time_end = process_time()
    time_elapsed = time_end - time_start

    return path, cost, time_elapsed


def _recurrent(current_node, nodes_left):
    if len(nodes_left) == 0:
        return [], 0.0

    best_path = []
    best_cost = float('inf')

    for node in nodes_left:
        subset = nodes_left.copy()
        subset.remove(node)
        subpath, subcost = _recurrent(node, subset)
        subcost += dist(current_node, node)

        if subcost < best_cost:
            best_cost = subcost
            best_path = [node] + subpath

    return best_path, best_cost
