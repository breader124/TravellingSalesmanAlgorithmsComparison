from time import process_time
import heapq

from misc import edges_from_nodes, dist_from_beginning, take_len
from heuristics import heuristic


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


def get_updated_states_vector(edges, states, expanded, nodes):
    heapq.heappop(states)
    for s in expanded:
        dist_from_beg = dist_from_beginning(s, nodes[0], len(nodes) + 1)
        cost = dist_from_beg + heuristic(edges, s, nodes)
        heapq.heappush(states, (cost, s))

    return states


def get_current_state(states):
    popped = heapq.heappop(states)
    current_state = popped[1]
    heapq.heappush(states, popped)

    return current_state
