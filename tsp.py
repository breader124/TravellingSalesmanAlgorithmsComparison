from argparse import ArgumentParser
from node import Node
from brute_force import brute_force


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('algorithm')

    args = parser.parse_args()
    return args.file, args.algorithm


def read_data(filename: str):
    nodes = []

    with open(filename, 'r') as file:
        for row in file:
            label, x, y = row.strip().split(' ')
            new_node = Node(label, float(x), float(y))
            nodes.append(new_node)

    return nodes


def main():
    file, algorithm = parse_args()
    nodes = read_data(file)

    if algorithm == 'bf':
        path, cost, time = brute_force(nodes)
    else:
        raise Exception(f'Algorithm {algorithm} not implemented!')

    print(path)
    print(cost)
    print(time)


if __name__ == '__main__':
    main()
