"""Lab 1 - Question 1: Linear Search implementation."""

import random
import time


def linear_search_353(arr_353, target_353):
    for index_353 in range(len(arr_353)):
        if arr_353[index_353] == target_353:
            return index_353
    return -1


INPUT_SIZES_353 = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
NUM_TRIALS_353 = 10


def generate_random_dataset_353(size_353):
    return [random.randint(0, size_353 * 10) for _ in range(size_353)]


def measure_linear_search_353(size_353):
    total_time_353 = 0.0
    for _ in range(NUM_TRIALS_353):
        dataset_353 = generate_random_dataset_353(size_353)
        target_353 = random.choice(dataset_353)
        start_353 = time.perf_counter()
        linear_search_353(dataset_353, target_353)
        end_353 = time.perf_counter()
        total_time_353 += end_353 - start_353
    return total_time_353, total_time_353 / NUM_TRIALS_353


if __name__ == "__main__":
    print("Linear Search - Execution Time")
    print(f"{'Size':>10} | {'Actual Time (s)':>20} | {'Average Time (s)':>20}")
    print("-" * 57)
    for size_353 in INPUT_SIZES_353:
        actual_time_353, avg_time_353 = measure_linear_search_353(size_353)
        print(f"{size_353:>10} | {actual_time_353:>20.8f} | {avg_time_353:>20.8f}")
