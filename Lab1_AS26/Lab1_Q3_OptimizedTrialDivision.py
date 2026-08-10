"""Lab 1 - Question 3: Optimized Trial Division (checking divisors up to sqrt(n))."""

import time


def is_prime_optimized_353(n_353):
    if n_353 < 2:
        return False
    if n_353 in (2, 3):
        return True
    if n_353 % 2 == 0:
        return False
    divisor_353 = 3
    while divisor_353 * divisor_353 <= n_353:
        if n_353 % divisor_353 == 0:
            return False
        divisor_353 += 2
    return True


def generate_primes_optimized_353(limit_353):
    primes_353 = []
    for num_353 in range(2, limit_353 + 1):
        if is_prime_optimized_353(num_353):
            primes_353.append(num_353)
    return primes_353


INPUT_SIZES_353 = [10000, 50000, 100000, 500000, 1000000]
NUM_TRIALS_353 = 3


def measure_optimized_353(limit_353):
    total_time_353 = 0.0
    for _ in range(NUM_TRIALS_353):
        start_353 = time.perf_counter()
        generate_primes_optimized_353(limit_353)
        end_353 = time.perf_counter()
        total_time_353 += end_353 - start_353
    return total_time_353, total_time_353 / NUM_TRIALS_353


if __name__ == "__main__":
    print("Optimized Trial Division - Execution Time")
    print(f"{'Limit':>10} | {'Actual Time (s)':>20} | {'Average Time (s)':>20}")
    print("-" * 57)
    for size_353 in INPUT_SIZES_353:
        actual_time_353, avg_time_353 = measure_optimized_353(size_353)
        print(f"{size_353:>10} | {actual_time_353:>20.8f} | {avg_time_353:>20.8f}")
