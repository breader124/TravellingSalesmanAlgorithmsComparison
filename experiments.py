from argparse import ArgumentParser
from csv import DictWriter
from glob import glob
from time import process_time
import os
import tracemalloc

from misc import read_data
from brute_force import BruteForce
from a_star import AStarAlgorithm
from greedy import GreedyAlgorithm


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('output_dir')
    parser.add_argument('--plot', action='store_true', help='Show plot')
    parser.add_argument(
        '-y', action='store_true', help='Compute all cases without asking')

    args = parser.parse_args()
    return args.directory, args.output_dir, args.plot, args.y


def plot_times(results, filename):
    from matplotlib import pyplot as plt
    import seaborn as sns
    sns.set()

    x = [result['n'] for result in results]

    y_bf = [result['BF'] for result in results]
    y_as = [result['A*'] for result in results]
    y_gr = [result['Greedy'] for result in results]

    sns.lineplot(x, y_bf)
    sns.lineplot(x, y_as)
    sns.lineplot(x, y_gr)

    plt.yscale('log')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time [s]')
    plt.legend(['Brute force', 'A*', 'Greedy'])

    plt.savefig(filename)
    plt.show()


def main():
    directory, output_dir, make_plot, force_yes = parse_args()
    results = []

    files = glob(f'{directory}/*.in')
    files.sort()
    experiment_start = process_time()
    tracemalloc.start()

    for i, file in enumerate(files):
        case_start = process_time()
        result = {}
        nodes = read_data(file)
        n = len(nodes)
        result['n'] = n

        # Brute Force
        solver = BruteForce(nodes)
        path, cost, time = solver.run()
        result['BF'] = time

        # A*
        solver = AStarAlgorithm(nodes)
        path, cost, time = solver.run()
        result['A*'] = time

        # Greedy
        solver = GreedyAlgorithm(nodes)
        path, cost, time = solver.run()
        result['Greedy'] = time

        case_end = process_time()
        case_time = case_end - case_start
        results.append(result)

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

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(f'{output_dir}/results.csv', 'w') as file:
        writer = DictWriter(file, results[0].keys())

        writer.writeheader()
        writer.writerows(results)

    if make_plot:
        plot_times(results, f'{output_dir}/results.png')


if __name__ == '__main__':
    main()
