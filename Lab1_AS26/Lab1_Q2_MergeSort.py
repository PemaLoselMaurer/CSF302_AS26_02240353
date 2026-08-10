"""Lab 1 - Question 2: Merge Sort implementation."""

import random
import time


def merge_353(left_353, right_353):
    result_353 = []
    i_353 = j_353 = 0
    while i_353 < len(left_353) and j_353 < len(right_353):
        if left_353[i_353] <= right_353[j_353]:
            result_353.append(left_353[i_353])
            i_353 += 1
        else:
            result_353.append(right_353[j_353])
            j_353 += 1
    result_353.extend(left_353[i_353:])
    result_353.extend(right_353[j_353:])
    return result_353


def merge_sort_353(arr_353):
    if len(arr_353) <= 1:
        return arr_353.copy()
    mid_353 = len(arr_353) // 2
    left_353 = merge_sort_353(arr_353[:mid_353])
    right_353 = merge_sort_353(arr_353[mid_353:])
    return merge_353(left_353, right_353)


INPUT_SIZES_353 = [100, 500, 1000, 2000, 4000, 8000]
NUM_TRIALS_353 = 5


def generate_random_array_353(size_353):
    return [random.randint(0, size_353 * 10) for _ in range(size_353)]


def measure_merge_sort_353(size_353):
    total_time_353 = 0.0
    for _ in range(NUM_TRIALS_353):
        array_353 = generate_random_array_353(size_353)
        start_353 = time.perf_counter()
        merge_sort_353(array_353)
        end_353 = time.perf_counter()
        total_time_353 += end_353 - start_353
    return total_time_353, total_time_353 / NUM_TRIALS_353


if __name__ == "__main__":
    print("Merge Sort - Execution Time")
    print(f"{'Size':>10} | {'Actual Time (s)':>20} | {'Average Time (s)':>20}")
    print("-" * 57)
    for size_353 in INPUT_SIZES_353:
        actual_time_353, avg_time_353 = measure_merge_sort_353(size_353)
        print(f"{size_353:>10} | {actual_time_353:>20.8f} | {avg_time_353:>20.8f}")
