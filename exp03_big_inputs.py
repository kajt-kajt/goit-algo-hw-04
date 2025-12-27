"""
Experiment 3 - relatively big input sizes
"""

import timeit
import random
import matplotlib.pyplot as plt
from settings import *

REPEATS_PER_TEST = 10

input_sizes = list(range(200,4_000,200))
results = { k:[] for k in algorithms }

for n in input_sizes:
    data_sample = [random.randint(0,1000) for _ in range(n)]
    for algo in algorithms:
        results[algo].append(timeit.timeit('algorithms[algo](data_sample[:])', number=REPEATS_PER_TEST, globals=globals()))

with open("./textfiles/big_input_size.md","w",encoding="utf-8") as f:
    algo_names = list(algorithms.keys())
    f.write("| Input size | " + " | ".join(algo_names) + " |\n")
    f.write("| " + "---- | "*(len(algo_names)+1) + "\n")
    for i in range(len(input_sizes)):
        line_to_write = f"| {input_sizes[i]} | "\
            + " | ".join([f"{results[algo][i]:.5f}" for algo in algo_names])\
            + " |\n"
        f.write(line_to_write)

fig, ax = plt.subplots()

for algo in algorithm_colors:
    ax.plot(input_sizes, results[algo], f'{algorithm_colors[algo]}o', label=algo, markersize=4)
    ax.plot(input_sizes, results[algo], f'{algorithm_colors[algo]}-', linewidth=1)

# Add labels and title
ax.set_xlabel('Input size')
ax.set_ylabel(f'Time for {REPEATS_PER_TEST} experiments, sec')
ax.set_title('Algorithms performance from input size')
ax.legend()
ax.grid(True)
plt.savefig("./pictures/big_input_size.png")
