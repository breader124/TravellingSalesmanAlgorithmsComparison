from argparse import ArgumentParser
from misc import read_data
from brute_force import brute_force


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('algorithm')

    args = parser.parse_args()
    return args.file, args.algorithm


def main():
    file, algorithm = parse_args()
    nodes = read_data(file)

    if algorithm == 'bf':
        path, cost, time = brute_force(nodes)
    else:
        raise Exception(f'Algorithm {algorithm} not implemented!')

    labels = [node.label for node in path]
    print(' '.join(labels))
    print(cost)
    print(time)


if __name__ == '__main__':
    main()
