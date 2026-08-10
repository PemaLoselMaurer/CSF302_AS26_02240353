"""Lab 1 - Question 3: Sieve of Eratosthenes implementation."""

import time


def sieve_of_eratosthenes_353(limit_353):
    if limit_353 < 2:
        return []
    is_prime_353 = [True] * (limit_353 + 1)
    is_prime_353[0] = is_prime_353[1] = False
    p_353 = 2
    while p_353 * p_353 <= limit_353:
        if is_prime_353[p_353]:
            for multiple_353 in range(p_353 * p_353, limit_353 + 1, p_353):
                is_prime_353[multiple_353] = False
        p_353 += 1
    return [num_353 for num_353, prime_flag_353 in enumerate(is_prime_353) if prime_flag_353]


INPUT_SIZES_353 = [10000, 50000, 100000, 500000, 1000000]
NUM_TRIALS_353 = 3


def measure_sieve_353(limit_353):
    total_time_353 = 0.0
    for _ in range(NUM_TRIALS_353):
        start_353 = time.perf_counter()
        sieve_of_eratosthenes_353(limit_353)
        end_353 = time.perf_counter()
        total_time_353 += end_353 - start_353
    return total_time_353, total_time_353 / NUM_TRIALS_353


if __name__ == "__main__":
    print("Sieve of Eratosthenes - Execution Time")
    print(f"{'Limit':>10} | {'Actual Time (s)':>20} | {'Average Time (s)':>20}")
    print("-" * 57)
    for size_353 in INPUT_SIZES_353:
        actual_time_353, avg_time_353 = measure_sieve_353(size_353)
        print(f"{size_353:>10} | {actual_time_353:>20.8f} | {avg_time_353:>20.8f}")
