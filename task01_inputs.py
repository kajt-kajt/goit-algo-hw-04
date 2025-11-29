import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import matplotlib.pyplot as plt

REPEATS_PER_TEST = 100

##################### Experiment 1 #############################
### Random input of different sizes ###

input_sizes = [10, 100, 200, 500, 1000, 2000]
sorted_result = []
insertion_result = []
merge_result = []

for n in input_sizes:
    data_sample = [random.randint(0,1000) for _ in range(n)]
    sorted_result.append(timeit.timeit('sorted(data_sample)', number=REPEATS_PER_TEST, globals=globals()))
    insertion_result.append(timeit.timeit('insertion_sort(data_sample[:])', number=REPEATS_PER_TEST, globals=globals()))
    merge_result.append(timeit.timeit('merge_sort(data_sample)', number=REPEATS_PER_TEST, globals=globals()))
    if n == 10:
        print(data_sample)
    print(n)
    
fig, ax = plt.subplots()

# Plot the points as markers
ax.plot(input_sizes, insertion_result, 'ro', label='Insertion Sort', markersize=8)
ax.plot(input_sizes, insertion_result, 'r-', linewidth=2)

ax.plot(input_sizes, merge_result, 'bo', label='Merge Sort', markersize=8)
ax.plot(input_sizes, merge_result, 'b-', linewidth=2)

ax.plot(input_sizes, sorted_result, 'ko', label='Python built-in', markersize=8)
ax.plot(input_sizes, sorted_result, 'k-', linewidth=2)

# Add labels and title
ax.set_xlabel('Input size')
ax.set_ylabel(f'Time for {REPEATS_PER_TEST} experiments, sec')
ax.set_title('Algorithms performance from input size')
ax.legend()
ax.grid(True)

# Display the plot
plt.show()

