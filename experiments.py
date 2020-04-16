from argparse import ArgumentParser
from csv import DictWriter
from glob import glob
from time import process_time
import tracemalloc

from misc import read_data
from brute_force import BruteForce
from a_star import AStarAlgorithm
from greedy import GreedyAlgorithm


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('--plot', action='store_true', help='Show plot')
    parser.add_argument(
        '-y', action='store_true', help='Compute all cases without asking')

    args = parser.parse_args()
    return args.directory, args.plot, args.y


def main():
    directory, make_plot, force_yes = parse_args()
    results = {
        'a-star': [],
        'bf': [],
        'greedy': [],
    }

    files = glob(f'{directory}/*.in')
    files.sort()
    experiment_start = process_time()
    tracemalloc.start()

    for i, file in enumerate(files):
        case_start = process_time()
        nodes = read_data(file)
        n = len(nodes)

        # Brute Force
        solver = BruteForce(nodes)
        path, cost, time = solver.run()
        results['bf'].append({'n': n, 'time': time})

        # A*
        solver = AStarAlgorithm(nodes)
        path, cost, time = solver.run()
        results['a-star'].append({'n': n, 'time': time})

        # Greedy
        solver = GreedyAlgorithm(nodes)
        path, cost, time = solver.run()
        results['greedy'].append({'n': n, 'time': time})

        case_end = process_time()
        case_time = case_end - case_start

        print(f'Case {i + 1}/{len(files)}: Finished {n} nodes in {case_time:.4f} seconds')
        if not force_yes and case_time > 60 and i + 1 < len(files):
            response = input('Continue? [Y/n]: ')
            if response == 'n':
                break

    experiment_stop = process_time()
    experiment_time = experiment_stop - experiment_start
    print(f'Finished experiments in {experiment_time:.2f} seconds')
    _, peak = tracemalloc.get_traced_memory()
    print(f'Peak memory usage: {(peak / 10**6):.1f}MB')

    for algo in results.keys():
        with open(f'results_{algo}.csv', 'w') as file:
            writer = DictWriter(file, ['n', 'time'])

            writer.writeheader()
            writer.writerows(results[algo])


if __name__ == '__main__':
    main()
