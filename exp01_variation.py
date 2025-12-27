"""
Experiment 1 - Multiple random input sizes for algorithms
Exploring the dispersion of performance
"""

import timeit
import random
import matplotlib.pyplot as plt
from settings import *

REPEATS_PER_TEST = 10
SAME_SIZE_INPUTS = 30

input_sizes = [100]*SAME_SIZE_INPUTS\
            + [250]*SAME_SIZE_INPUTS\
            + [500]*SAME_SIZE_INPUTS\
            + [750]*SAME_SIZE_INPUTS\
            + [1000]*SAME_SIZE_INPUTS

for algo in algorithms:
    algo_result = []
    for n in input_sizes:
        data_sample = [random.randint(0,1000) for _ in range(n)]
        algo_result.append(timeit.timeit('algorithms[algo](data_sample[:])', number=REPEATS_PER_TEST, globals=globals()))
    with open(f"./textfiles/{algo}_variation.md","w",encoding="utf-8") as f:
        f.write(f"| Input size | {algo} |\n")
        f.write("| ---- | ---- |\n")
        for i in range(len(input_sizes)//SAME_SIZE_INPUTS):
            res = ", ".join([f"{val:.5f}" for val in algo_result[SAME_SIZE_INPUTS*i:SAME_SIZE_INPUTS*(i+1)]])
            f.write(f"| {input_sizes[SAME_SIZE_INPUTS*i]} | {res} |\n")
    fig, ax = plt.subplots()
    ax.plot(input_sizes, algo_result, algorithm_colors[algo]+"o", label=f'{algo} variation', markersize=4)
    # Add labels and title
    ax.set_xlabel('Input size')
    ax.set_ylabel(f'Time for {REPEATS_PER_TEST} experiments, sec')
    ax.set_title(f'Algorithm {algo} variation with random inputs')
    ax.legend()
    ax.grid(True)
    plt.savefig(f"./pictures/{algo}_variation.png")
    # plt.show()
