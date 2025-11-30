"""
Experiment 1 - small input sizes
"""

import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import matplotlib.pyplot as plt

REPEATS_PER_TEST = 100

input_sizes = list(range(10,250,10))
sorted_result = []
insertion_result = []
merge_result = []

for n in input_sizes:
    data_sample = [random.randint(0,1000) for _ in range(n)]
    sorted_result.append(timeit.timeit('sorted(data_sample)', number=REPEATS_PER_TEST, globals=globals()))
    insertion_result.append(timeit.timeit('insertion_sort(data_sample[:])', number=REPEATS_PER_TEST, globals=globals()))
    merge_result.append(timeit.timeit('merge_sort(data_sample)', number=REPEATS_PER_TEST, globals=globals()))
   
print("| Input size | Insertion sort | Merge sort | Built-in |")
print("| ---- | ---- | ---- | ---- |")
for i in range(len(input_sizes)):
    print(f"| {input_sizes[i]} | {insertion_result[i]:.5f} | {merge_result[i]:.5f} | {sorted_result[i]:.5f} |")

fig, ax = plt.subplots()

ax.plot(input_sizes, insertion_result, 'ro', label='Insertion Sort', markersize=4)
ax.plot(input_sizes, insertion_result, 'r-', linewidth=1)

ax.plot(input_sizes, merge_result, 'bo', label='Merge Sort', markersize=4)
ax.plot(input_sizes, merge_result, 'b-', linewidth=1)

ax.plot(input_sizes, sorted_result, 'ko', label='Python built-in', markersize=4)
ax.plot(input_sizes, sorted_result, 'k-', linewidth=1)

# Add labels and title
ax.set_xlabel('Input size')
ax.set_ylabel(f'Time for {REPEATS_PER_TEST} experiments, sec')
ax.set_title('Algorithms performance from input size')
ax.legend()
ax.grid(True)

# Display the plot
plt.show()

