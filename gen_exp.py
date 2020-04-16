import os
from random import uniform

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('n')
    parser.add_argument('directory')

    args = parser.parse_args()
    return int(args.n), args.directory


BOUNDARY = 100

if __name__ == '__main__':
    n, directory = parse_args()

    if not os.path.exists(directory):
        os.mkdir(directory)

    for i in range(2, n + 1):
        with open(f'{directory}/{i:02}.in', 'w') as file:
            for j in range(i):
                x = uniform(-BOUNDARY, BOUNDARY)
                y = uniform(-BOUNDARY, BOUNDARY)
                file.write(f'{j} {x} {y}\n')
