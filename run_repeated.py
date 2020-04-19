from argparse import ArgumentParser
from csv import DictWriter
from glob import glob

from single_experiment import single_experiment


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('input_dir')
    parser.add_argument('algo')
    parser.add_argument('n')

    args = parser.parse_args()
    return args.input_dir, args.algo, int(args.n)


def main():
    input_dir, algo, repeats = parse_args()
    output_file = f'results_{algo}.csv'

    files = glob(f'{input_dir}/*.in')
    files.sort()

    with open(output_file, 'w') as csv_file:
        writer = DictWriter(csv_file, fieldnames=['n', 'time'])
        writer.writeheader()

        for file in files:
            print(f'Starting {file}:')
            times = []
            mems = []
            costs = []

            for i in range(repeats):
                nodes_no, time, cost, memory = single_experiment(file, algo)
                writer.writerow({'n': nodes_no, 'time': time})
                print(f'    Finished {i + 1}/{repeats}')

                times.append(time)
                mems.append(memory)
                costs.append(cost)

            mean_time = sum(times) / len(times)
            mean_cost = sum(costs) / len(costs)
            mean_mem = sum(mems) / len(mems)
            print(f'    * Mean time {mean_time:.4f} seconds')
            print(f'    * Mean cost {mean_cost:.4f}')
            print(f'    * Mean peak memory: {(mean_mem / 10 ** 6):.1f}MB')
            print(f'Finished {file}')


if __name__ == '__main__':
    main()
