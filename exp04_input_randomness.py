"""
Experiment 3 - relatively big input sizes
"""

import timeit
import random
import matplotlib.pyplot as plt
from settings import *

REPEATS_PER_TEST = 10
INPUT_SIZE = 1000
PERMUTATIONS = 3*INPUT_SIZE
STEP = 5

data_sample = list(range(0,INPUT_SIZE))
results = { k:[] for k in algorithms }

for i in range(STEP, PERMUTATIONS, STEP):
    print(i)
    for _ in range(STEP):
        ind1 = random.randint(0,len(data_sample)-1)
        ind2 = random.randint(0,len(data_sample)-1)
        data_sample[ind1], data_sample[ind2] = data_sample[ind2], data_sample[ind1]
    for algo in algorithms:
        results[algo].append(timeit.timeit('algorithms[algo](data_sample[:])', number=REPEATS_PER_TEST, globals=globals()))

with open(f"./textfiles/{INPUT_SIZE}_permutations.md","w",encoding="utf-8") as f:
    algo_names = list(algorithms.keys())
    f.write("| Input size | " + " | ".join(algo_names) + " |\n")
    f.write("| " + "---- | "*(len(algo_names)+1) + "\n")
    for i in range(PERMUTATIONS//STEP - 1):
        line_to_write = f"| {i*STEP} | "\
            + " | ".join([f"{results[algo][i]:.5f}" for algo in algo_names])\
            + " |\n"
        f.write(line_to_write)

fig, ax = plt.subplots()

for algo in algorithm_colors:
    ax.plot(list(range(STEP, PERMUTATIONS, STEP)), results[algo], f'{algorithm_colors[algo]}o', label=algo, markersize=4)
    ax.plot(list(range(STEP, PERMUTATIONS, STEP)), results[algo], f'{algorithm_colors[algo]}-', linewidth=1)

# Add labels and title
ax.set_xlabel('Permutations in pre-sorted input')
ax.set_ylabel(f'Time for {REPEATS_PER_TEST} experiments, sec')
ax.set_title('Algorithms performance from input randomness')
ax.legend()
ax.grid(True)
plt.savefig(f"./pictures/{INPUT_SIZE}_permutations.png")
