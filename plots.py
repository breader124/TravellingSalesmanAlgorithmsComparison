from argparse import ArgumentParser
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('out_file')

    args = parser.parse_args()
    return args.out_file


def main():
    out_file = parse_args()
    as_file = 'results_a-star.csv'
    bf_file = 'results_bf.csv'
    gr_file = 'results_greedy.csv'

    as_df = pd.read_csv(as_file)
    bf_df = pd.read_csv(bf_file)
    gr_df = pd.read_csv(gr_file)
    dfs = [as_df, bf_df, gr_df]

    for df in dfs:
        sns.lineplot(x='n', y='time', data=df, ci='sd')

    plt.yscale('log')
    plt.legend(['A*', 'Brute force', 'Greedy'])
    plt.xlabel('Number of nodes')
    plt.ylabel('Time [s]')

    plt.savefig(out_file, dpi=300)
    plt.show()


if __name__ == '__main__':
    main()
