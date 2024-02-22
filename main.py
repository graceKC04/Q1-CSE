import timeit
import random
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def merge_sort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def test_sorting_algorithms(start, end, step, num_trials):
    sizes = []
    insertion_avg_times = []
    merge_avg_times = []

    for size in range(start, end + 1, step):
        sizes.append(size)
        insertion_times = []
        merge_times = []

        for _ in range(num_trials):
            #Randomly generate array
            arr = [random.randint(1, 100) for _ in range(size)]

            # Measure insertion sort time
            insertion_arr = arr.copy()
            insertion_time = timeit.timeit(lambda: insertion_sort(insertion_arr), number=1)
            insertion_times.append(insertion_time)

            # Measure merge sort time
            merge_arr = arr.copy()
            right = len(merge_arr) - 1
            merge_time = timeit.timeit(lambda: merge_sort(merge_arr, 0, right), number=1)
            merge_times.append(merge_time)

        insertion_avg_times.append(np.mean(insertion_times))
        merge_avg_times.append(np.mean(merge_times))

    return sizes, insertion_avg_times, merge_avg_times

start_size = 1
end_size = 200
step = 5
num_trials = 1000

sizes, insertion_avg_times, merge_avg_times = test_sorting_algorithms(start_size, end_size, step, num_trials)

plt.plot(sizes, insertion_avg_times, label='Insertion Sort')
plt.plot(sizes, merge_avg_times, label='Merge Sort')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Insertion Sort and Merge Sort')
plt.legend()
plt.show()