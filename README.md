# Travelling Salesman Algorithms Comparison
Comparison of different algorithms for solving TSP.
Current implementations: TODO.

# Dependencies
If you want to plot results you need `matplotlib`:
```bash
python3 -m venv venv    # create new virtual environment
. venv/bin/activate     # activate
pip install matplotlib  # download matplotlib
```

# Run
Run with `python3 tsp.py {input_file} {algorithm}`.
Algorithms:
* TODO

Program shows plot with solution by default.
If you want only text output you can add `--text` option.

## Input format
Program reads file where each line has the following format: `label x_coordinate y_coordinate`.

## Output format
First line contains an itinerary that minimizes the total distance.
Second line contains total cost of itinerary.
Third line contains computation time in seconds.

# Data
Data in `cases` directory comes from
[people.sc.fsu.edu](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html)
and [math.uwaterloo.ca](http://www.math.uwaterloo.ca/tsp/).
