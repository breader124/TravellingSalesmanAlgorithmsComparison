from misc import edges_from_nodes, take_len


def heuristic(edges, state, nodes):
    span_tree = False
    if span_tree:
        return kruskal_algorithm(nodes)
    else:
        nodes_left = len(nodes) - len(state) + 1
        return min_edge_len_between_not_used_nodes(edges, state) * nodes_left


def kruskal_algorithm(nodes):
    msp_tree_dist = 0

    edges = edges_from_nodes(nodes)

    edges.sort(key=take_len)

    same_nodes = set()
    while edges and len(same_nodes) < len(nodes):
        current_edge = edges[0]
        if current_edge.first_node not in same_nodes or current_edge.second_node not in same_nodes:
            same_nodes.add(current_edge.first_node)
            same_nodes.add(current_edge.second_node)
            msp_tree_dist = msp_tree_dist + current_edge.length

        edges.remove(current_edge)

    return msp_tree_dist


def min_edge_len_between_not_used_nodes(edges, state):
    for edge in edges:
        if not edge_used(edge, state):
            return edge.length
    return 0.0


def edge_used(edge, state):
    try:
        first = state.index(edge.first_node.label)
        second = state.index(edge.first_node.label)
        return abs(first - second) == 1
    except ValueError:
        return False
