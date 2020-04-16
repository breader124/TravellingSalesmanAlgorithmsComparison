from argparse import ArgumentParser
import os
import tracemalloc

from misc import read_data
from brute_force import brute_force
from a_star import a_star
# from greedy import GreedyAlgorithm


def single_experiment(input_file, algo):
    tracemalloc.start()

    nodes = read_data(input_file)
    n = len(nodes)

    if algo == 'bf':
        path, cost, time = brute_force(nodes)
    elif algo == 'a-star':
        path, cost, time = a_star(nodes)
    # elif algo == 'greedy':
    #     solver = GreedyAlgorithm(nodes)
    else:
        raise Exception(f'Algorithm {algo} not implemented!')

    _, peak = tracemalloc.get_traced_memory()

    return n, time, peak
