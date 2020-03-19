from argparse import ArgumentParser
from misc import read_data
from brute_force import brute_force
from a_star import a_star


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('algorithm')
    parser.add_argument('--text', action='store_true', help='Don\'t show plot')

    args = parser.parse_args()
    return args.file, args.algorithm, args.text


def plot_path(path):
    from matplotlib import pyplot as plt
    x = [node.x for node in path]
    y = [node.y for node in path]
    plt.plot(x, y, 'rx', markersize=6)
    plt.plot(x, y, 'g--', lineWidth=1)
    plt.show()


def main():
    file, algorithm, text_only = parse_args()
    nodes = read_data(file)

    if algorithm == 'bf':
        path, cost, time = brute_force(nodes)
    elif algorithm == 'a-star':
        path, cost, time = a_star(nodes)
    else:
        raise Exception(f'Algorithm {algorithm} not implemented!')

    labels = [node.label for node in path]
    print(' '.join(labels))
    print(cost)
    print(time)

    if not text_only:
        plot_path(path)


if __name__ == '__main__':
    main()
