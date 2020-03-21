from math import sqrt


class Node:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __lt__(self, other):
        return True


class Edge:
    def __init__(self, first_node, second_node, length):
        self.first_node = first_node
        self.second_node = second_node
        self.length = length


def read_data(filename: str):
    nodes = []

    with open(filename, 'r') as file:
        for row in file:
            label, x, y = row.strip().split(' ')
            new_node = Node(label, float(x), float(y))
            nodes.append(new_node)

    return nodes


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


def dist_from_beginning(state, start_node, total_size):
    if chose_home_too_early(state, start_node, total_size):
        return float('inf')

    d = 0
    for i in range(1, len(state)):
        d = d + dist(state[i - 1], state[i])

    return d


def dist(a: Node, b: Node):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def chose_home_too_early(state, start_node, total_size):
    return len(state) < total_size and state[-1] == start_node


def take_len(edge):
    return edge.length
