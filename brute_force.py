from time import process_time
from misc import dist


def brute_force(nodes):
    time_start = process_time()

    first_node = nodes[0]
    path, cost = _recurrent(first_node, first_node, nodes[1:])
    path = [first_node] + path

    time_end = process_time()
    time_elapsed = time_end - time_start

    return path, cost, time_elapsed


def _recurrent(first_node, current_node, nodes_left):
    if len(nodes_left) == 0:
        return [first_node], dist(current_node, first_node)

    best_path = []
    best_cost = float('inf')

    for node in nodes_left:
        subset = nodes_left.copy()
        subset.remove(node)
        subpath, subcost = _recurrent(first_node, node, subset)
        subcost += dist(current_node, node)

        if subcost < best_cost:
            best_cost = subcost
            best_path = [node] + subpath

    return best_path, best_cost
