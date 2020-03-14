class Node:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y


def read_data(filename: str):
    nodes = []

    with open(filename, 'r') as file:
        for row in file:
            label, x, y = row.strip().split(' ')
            new_node = Node(label, float(x), float(y))
            nodes.append(new_node)

    return nodes
