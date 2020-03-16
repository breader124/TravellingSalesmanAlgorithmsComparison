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


def dist(a: Node, b: Node):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def read_data(filename: str):
    nodes = []

    with open(filename, 'r') as file:
        for row in file:
            label, x, y = row.strip().split(' ')
            new_node = Node(label, float(x), float(y))
            nodes.append(new_node)

    return nodes
