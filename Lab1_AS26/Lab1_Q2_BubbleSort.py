"""Lab 1 - Question 2: Bubble Sort implementation."""

import random
import time


def bubble_sort_353(arr_353):
    array_353 = arr_353.copy()
    n_353 = len(array_353)
    for i_353 in range(n_353):
        swapped_353 = False
        for j_353 in range(0, n_353 - i_353 - 1):
            if array_353[j_353] > array_353[j_353 + 1]:
                array_353[j_353], array_353[j_353 + 1] = array_353[j_353 + 1], array_353[j_353]
                swapped_353 = True
        if not swapped_353:
            break
    return array_353


INPUT_SIZES_353 = [100, 500, 1000, 2000, 4000, 8000]
NUM_TRIALS_353 = 5


def generate_random_array_353(size_353):
    return [random.randint(0, size_353 * 10) for _ in range(size_353)]


def measure_bubble_sort_353(size_353):
    total_time_353 = 0.0
    for _ in range(NUM_TRIALS_353):
        array_353 = generate_random_array_353(size_353)
        start_353 = time.perf_counter()
        bubble_sort_353(array_353)
        end_353 = time.perf_counter()
        total_time_353 += end_353 - start_353
    return total_time_353, total_time_353 / NUM_TRIALS_353


if __name__ == "__main__":
    print("Bubble Sort - Execution Time")
    print(f"{'Size':>10} | {'Actual Time (s)':>20} | {'Average Time (s)':>20}")
    print("-" * 57)
    for size_353 in INPUT_SIZES_353:
        actual_time_353, avg_time_353 = measure_bubble_sort_353(size_353)
        print(f"{size_353:>10} | {actual_time_353:>20.8f} | {avg_time_353:>20.8f}")
