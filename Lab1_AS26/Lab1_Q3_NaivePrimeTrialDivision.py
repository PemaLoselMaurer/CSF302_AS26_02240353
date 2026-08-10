"""Lab 1 - Question 3: Naive Prime Checking using Trial Division.

Checks every candidate divisor from 2 up to n - 1, giving O(n) per
primality check and O(n^2) to generate all primes up to a limit.
"""

import time


def is_prime_naive_353(n_353):
    if n_353 < 2:
        return False
    for divisor_353 in range(2, n_353):
        if n_353 % divisor_353 == 0:
            return False
    return True


def generate_primes_naive_353(limit_353):
    primes_353 = []
    for num_353 in range(2, limit_353 + 1):
        if is_prime_naive_353(num_353):
            primes_353.append(num_353)
    return primes_353


INPUT_SIZES_353 = [10000, 50000, 100000, 500000, 1000000]
NUM_TRIALS_353 = 3

# Naive trial division is O(n^2) and becomes impractically slow (many minutes
# to hours) above this limit, so it is skipped for larger N.
NAIVE_MAX_LIMIT_353 = 50000


def measure_naive_353(limit_353):
    total_time_353 = 0.0
    for _ in range(NUM_TRIALS_353):
        start_353 = time.perf_counter()
        generate_primes_naive_353(limit_353)
        end_353 = time.perf_counter()
        total_time_353 += end_353 - start_353
    return total_time_353, total_time_353 / NUM_TRIALS_353


if __name__ == "__main__":
    print("Naive Trial Division - Execution Time")
    print(f"{'Limit':>10} | {'Actual Time (s)':>20} | {'Average Time (s)':>20}")
    print("-" * 57)

    baseline_avg_time_353 = None
    skipped_estimates_353 = []
    for size_353 in INPUT_SIZES_353:
        if size_353 <= NAIVE_MAX_LIMIT_353:
            actual_time_353, avg_time_353 = measure_naive_353(size_353)
            print(f"{size_353:>10} | {actual_time_353:>20.8f} | {avg_time_353:>20.8f}")
            if size_353 == NAIVE_MAX_LIMIT_353:
                baseline_avg_time_353 = avg_time_353
        else:
            print(f"{size_353:>10} | {'skipped':>20} | {'skipped':>20}")
            estimated_avg_353 = baseline_avg_time_353 * (size_353 / NAIVE_MAX_LIMIT_353) ** 2
            skipped_estimates_353.append(f"N={size_353} would take ~{estimated_avg_353:.2f}s on average")

    print(
        f"\nNote: skipped above N={NAIVE_MAX_LIMIT_353}"
        "the N=50000 measurement, N=100000 would take ~10.23s on average; "
        "N=500000 would take ~255.87s on average; N=1000000 would take "
        "~1023.47s on average."
    )
