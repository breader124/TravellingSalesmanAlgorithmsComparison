import unittest
import os
from misc import read_data
from a_star import AStarAlgorithm

cases_cut = 'cases_cut'


class MyTestCase(unittest.TestCase):
    def test_a_star(self):
        for filename in os.listdir(cases_cut):
            if filename.endswith('.out'):
                continue

            full_path = "{}/{}".format(cases_cut, filename)

            computed_path, computed_cost = run_a_star(full_path)
            given_res_path, given_res_cost = load_given_results(filename)

            self.assertIn(given_res_path, computed_path, filename)
            self.assertEqual(given_res_cost, computed_cost, filename)


def run_a_star(path_to_file):
    nodes = read_data(path_to_file)

    algorithm = AStarAlgorithm(nodes)
    path_nodes, cost, time = algorithm.run()

    path = get_path_and_path_reversed(path_nodes)
    cost = round(cost, 2)

    return path, cost


def get_path_and_path_reversed(path):
    path_labels = [node.label for node in path]
    same = ' '.join(path_labels)

    path_labels.reverse()
    rev = ' '.join(path_labels)

    return [same, rev]


def load_given_results(filename):
    out_filename = filename.replace('.in', '.out')
    out_path = "{}/{}".format(cases_cut, out_filename)
    return get_res_under_path(out_path)


def get_res_under_path(path):
    file = open(path)
    lines = file.readlines()

    path = lines[0].strip()
    cost = float(lines[1])
    cost = round(cost, 2)

    file.close()

    return path, cost


if __name__ == '__main__':
    unittest.main()
