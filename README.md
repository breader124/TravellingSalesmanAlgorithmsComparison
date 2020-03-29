# Travelling Salesman Algorithms Comparison
Comparison of different algorithms for solving TSP.
Current implementations: TODO.

# Dependencies
If you want to plot results you need `matplotlib` and `seaborn`:
```bash
python3 -m venv venv    # create new virtual environment
. venv/bin/activate     # activate
pip install matplotlib seaborn  # download matplotlib
```

# Run single
Run with `python3 tsp.py {input_file} {algorithm}`.
Algorithms:
* `bf` - brute force, checks all permutations.
Time O(n!). Warning: for just 12 nodes it runs for approximately 1 minute.

Program shows plot with solution by default.
If you want only text output you can add `--text` option.

## Input format
Program reads file where each line has the following format: `label x_coordinate y_coordinate`.

## Output format
First line contains an itinerary that minimizes the total distance.
Second line contains total cost of itinerary.
Third line contains computation time in seconds.

# Compare
Generate test cases using `python gen_exp.py {max_number_of_nodes} {output_directory}`.

You can run all experiments with `python experiments.py {input_folder} [-y] [--plot]`.

You can run repeated experiments for single algorithm using `python run_repeated.py {input_folder} {bf/a-star/greedy} {number_of_repeats}`.

Make a plot using `python plots.py {output_file}`.

# Data
Data in `cases` directory comes from
[people.sc.fsu.edu](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html)
and [math.uwaterloo.ca](http://www.math.uwaterloo.ca/tsp/).
