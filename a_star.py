from time import process_time
from misc import dist
from misc import Edge
import heapq


def a_star(nodes):
    edges = edges_from_nodes(nodes)
    edges.sort(key=take_len)

    time_start = process_time()

    current_state = [nodes[0]]
    states = []
    heapq.heappush(states, (0, current_state))

    while not is_terminal_state(current_state, nodes):
        nodes_left = get_nodes_left(nodes, current_state)
        current_expanded = get_expanded_state(current_state, nodes_left)
        states = get_updated_states_vector(edges, states, current_expanded, nodes)
        current_state = get_current_state(states)

    path, cost = current_state, dist_from_beginning(current_state, nodes[0], len(nodes))

    time_end = process_time()
    time_elapsed = time_end - time_start

    return path, cost, time_elapsed


def is_terminal_state(current_state, nodes):
    return len(set(current_state)) == len(nodes) and current_state[-1] == nodes[0]


def get_nodes_left(nodes, current_state):
    nodes_left = set(nodes).difference(current_state)
    nodes_left = list(nodes_left)
    nodes_left.append(nodes[0])

    return nodes_left


def get_expanded_state(current_state, nodes_left):
    expanded = []

    for node in nodes_left:
        expanded.append([*current_state, node])

    return expanded


def get_current_state(states):
    popped = heapq.heappop(states)
    current_state = popped[1]
    heapq.heappush(states, popped)

    return current_state


def get_updated_states_vector(edges, states, expanded, nodes):
    heapq.heappop(states)
    for s in expanded:
        dist_from_beg = dist_from_beginning(s, nodes[0], len(nodes) + 1)
        cost = dist_from_beg + heuristic(edges, s, nodes)
        heapq.heappush(states, (cost, s))

    return states


def dist_from_beginning(state, start_node, total_size):
    if chose_home_too_early(state, start_node, total_size):
        return float('inf')

    d = 0
    for i in range(1, len(state)):
        d = d + dist(state[i - 1], state[i])

    return d


def chose_home_too_early(state, start_node, total_size):
    return len(state) < total_size and state[-1] == start_node


def heuristic(edges, state, nodes):
    return min_edge_len_between_not_used_nodes(edges, state, nodes) * (len(nodes) - len(state) + 1)


# def kruskal_algorithm(nodes):
#     msp_tree_dist = 0
#
#     edges = edges_from_nodes(nodes)
#
#     edges.sort(key=take_len)
#
#     same_nodes = set()
#     while edges and len(same_nodes) < len(nodes):
#         current_edge = edges[0]
#         if current_edge.first_node not in same_nodes or current_edge.second_node not in same_nodes:
#             same_nodes.add(current_edge.first_node)
#             same_nodes.add(current_edge.second_node)
#             msp_tree_dist = msp_tree_dist + current_edge.length
#
#         edges.remove(current_edge)
#
#     return msp_tree_dist


def edges_from_nodes(nodes):
    nodes = list(nodes)
    second = nodes.copy()
    second.reverse()
    edges = []

    for first_node in nodes:
        second.pop()
        for second_node in second:
            edge_len = dist(first_node, second_node)
            edges.append(Edge(first_node, second_node, edge_len))

    return edges


def min_edge_len_between_not_used_nodes(edges, state, nodes):
    if one_node_from_path_left(state, nodes):
        node_left = set(nodes).difference().pop()
        return min(dist(state[-1], node_left), dist(node_left, nodes[0]))

    elif full_path_done(state, nodes):
        return dist(state[-1], nodes[0])

    elif at_the_beginning(state, nodes):
        return 0

    else:
        for edge in edges:
            if not node_used(edge, state):
                return edge.length


def one_node_from_path_left(state, nodes):
    return len(state) == len(nodes) - 1


def full_path_done(state, nodes):
    return len(state) == len(nodes)


def at_the_beginning(state, nodes):
    return len(state) == len(nodes) + 1


def node_used(edge, state):
    state = [s.label for s in state]
    return (edge.first_node.label in state) or (edge.second_node.label in state)


def take_len(edge):
    return edge.length

