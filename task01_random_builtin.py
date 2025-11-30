"""
Experiment 3 - Multiple random input sizes for built-in sort
"""

import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import matplotlib.pyplot as plt

REPEATS_PER_TEST = 10

input_sizes = [100]*20 + [250]*20 + [500]*20 + [750]*20 + [1000]*20
sorted_result = []

for n in input_sizes:
    data_sample = [random.randint(0,1000) for _ in range(n)]
    sorted_result.append(timeit.timeit('sorted(data_sample)', number=REPEATS_PER_TEST, globals=globals()))
    print(n)
   
print("| Input size | Built-in |")
print("| ---- | ---- |")
for i in range(len(input_sizes)//20):
    res = ", ".join([f"{val:.5f}" for val in sorted_result[20*i:20*(i+1)]])
    print(f"| {input_sizes[20*i]} | {res} |")

fig, ax = plt.subplots()

ax.plot(input_sizes, sorted_result, 'ko', label='Python built-in', markersize=4)

# Add labels and title
ax.set_xlabel('Input size')
ax.set_ylabel(f'Time for {REPEATS_PER_TEST} experiments, sec')
ax.set_title('Algorithms performance from input size')
ax.legend()
ax.grid(True)

# Display the plot
plt.show()

