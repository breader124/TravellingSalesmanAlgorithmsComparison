from argparse import ArgumentParser
import os
import tracemalloc

from misc import read_data
from brute_force import BruteForce
from a_star import AStarAlgorithm
from greedy import GreedyAlgorithm


def single_experiment(input_file, algo):
    tracemalloc.start()

    nodes = read_data(input_file)
    n = len(nodes)

    if algo == 'bf':
        solver = BruteForce(nodes)
    elif algo == 'a-star':
        solver = AStarAlgorithm(nodes)
    elif algo == 'greedy':
        solver = GreedyAlgorithm(nodes)
    else:
        raise Exception(f'Algorithm {algo} not implemented!')

    _, cost, time = solver.run()

    _, peak = tracemalloc.get_traced_memory()

    return n, time, cost, peak
