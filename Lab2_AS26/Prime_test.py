import math
import time
import matplotlib.pyplot as plt

def naive_prime_353(n_353):
    steps_353 = 0

    if n_353 < 2:
        return False, steps_353

    for i_353 in range(2, n_353):
        steps_353 += 1
        if n_353 % i_353 == 0:
            return False, steps_353

    return True, steps_353

def optimized_prime_353(n_353):
    steps_353 = 0

    if n_353 < 2:
        return False, steps_353

    limit_353 = int(math.sqrt(n_353))

    for i_353 in range(2, limit_353 + 1):
        steps_353 += 1
        if n_353 % i_353 == 0:
            return False, steps_353

    return True, steps_353

def sieve_353(limit_353):
    steps_353 = 0
    is_prime_353 = [True] * (limit_353 + 1)
    is_prime_353[0] = False
    if limit_353 >= 1:
        is_prime_353[1] = False

    p_353 = 2
    while p_353 * p_353 <= limit_353:
        if is_prime_353[p_353]:
            for multiple_353 in range(p_353 * p_353, limit_353 + 1, p_353):
                steps_353 += 1
                is_prime_353[multiple_353] = False
        p_353 += 1

    primes_353 = [i_353 for i_353 in range(2, limit_353 + 1) if is_prime_353[i_353]]
    return primes_353, steps_353

def time_it_353(func_353, n_353):
    start_353 = time.perf_counter()
    result_353, steps_353 = func_353(n_353)
    end_353 = time.perf_counter()
    micro_sec_353 = (end_353 - start_353) * 1_000_000
    return result_353, steps_353, micro_sec_353

def read_numbers_353():
    print("Enter at least 10 numbers separated by spaces")
    print("(press Enter to use the sample list):")
    line_353 = input("> ").strip()

    if line_353 == "":
        numbers_353 = [7, 97, 561, 1009, 5003, 10007, 20011, 49999, 99991, 199999]
        print("Using sample numbers:", numbers_353)
        return numbers_353

    numbers_353 = [int(x_353) for x_353 in line_353.split()]

    while len(numbers_353) < 10:
        print("Only", len(numbers_353), "entered. Please add more numbers.")
        extra_353 = input("> ").strip()
        numbers_353 += [int(x_353) for x_353 in extra_353.split()]

    return numbers_353

def main_353():
    numbers_353 = read_numbers_353()

    naive_steps_353 = []
    opt_steps_353 = []
    naive_time_353 = []
    opt_time_353 = []

    print("\n" + "-" * 78)
    print(f"{'Number':>10} {'Prime?':>8} {'Naive steps':>13} {'Opt steps':>11}"
          f" {'Naive us':>11} {'Opt us':>9}")
    print("-" * 78)

    for n_353 in numbers_353:
        r1_353, s1_353, t1_353 = time_it_353(naive_prime_353, n_353)
        r2_353, s2_353, t2_353 = time_it_353(optimized_prime_353, n_353)

        naive_steps_353.append(s1_353)
        opt_steps_353.append(s2_353)
        naive_time_353.append(t1_353)
        opt_time_353.append(t2_353)

        print(f"{n_353:>10} {('YES' if r1_353 else 'NO'):>8} {s1_353:>13}"
              f" {s2_353:>11} {t1_353:>11.2f} {t2_353:>9.2f}")

    print("-" * 78)
    print(f"{'TOTAL':>10} {'':>8} {sum(naive_steps_353):>13} {sum(opt_steps_353):>11}"
          f" {sum(naive_time_353):>11.2f} {sum(opt_time_353):>9.2f}")

    limit_353 = max(numbers_353)
    if limit_353 > 200000:
        limit_353 = 200000
    primes_353, sieve_step_353 = sieve_353(limit_353)
    print(f"\nSieve of Eratosthenes up to {limit_353}:")
    print(f"  total primes found : {len(primes_353)}")
    print(f"  first 15 primes    : {primes_353[:15]}")
    print(f"  steps used         : {sieve_step_353}")

    print("\nConclusion:")
    print("  Naive     -> O(n)       steps grow linearly with n")
    print("  Optimized -> O(sqrt n)  steps grow much more slowly")
    if sum(opt_steps_353) < sum(naive_steps_353):
        print("  => The OPTIMIZED (sqrt n) method is faster.")
    else:
        print("  => The NAIVE method used fewer steps for this input.")

    plot_graph_353(numbers_353, naive_steps_353, opt_steps_353,
                   naive_time_353, opt_time_353)

def plot_graph_353(numbers_353, naive_steps_353, opt_steps_353,
                   naive_time_353, opt_time_353):
    data_353 = sorted(zip(numbers_353, naive_steps_353, opt_steps_353,
                          naive_time_353, opt_time_353))
    x_353 = [d_353[0] for d_353 in data_353]
    ns_353 = [d_353[1] for d_353 in data_353]
    os_353 = [d_353[2] for d_353 in data_353]
    nt_353 = [d_353[3] for d_353 in data_353]
    ot_353 = [d_353[4] for d_353 in data_353]

    fig_353, ax_353 = plt.subplots(1, 2, figsize=(12, 5))

    ax_353[0].plot(x_353, ns_353, "o-", color="crimson", label="Naive  O(n)")
    ax_353[0].plot(x_353, os_353, "s-", color="seagreen", label="Optimized  O(sqrt n)")
    ax_353[0].set_title("Step count comparison")
    ax_353[0].set_xlabel("Number n")
    ax_353[0].set_ylabel("Steps (log scale)")
    ax_353[0].set_yscale("log")
    ax_353[0].legend()
    ax_353[0].grid(True, alpha=0.3)

    ax_353[1].plot(x_353, nt_353, "o-", color="crimson", label="Naive  O(n)")
    ax_353[1].plot(x_353, ot_353, "s-", color="seagreen", label="Optimized  O(sqrt n)")
    ax_353[1].set_title("Running time comparison")
    ax_353[1].set_xlabel("Number n")
    ax_353[1].set_ylabel("Time (microseconds)")
    ax_353[1].legend()
    ax_353[1].grid(True, alpha=0.3)

    fig_353.suptitle("Prime Testing: Naive vs Optimized (353)")
    fig_353.tight_layout()
    fig_353.savefig("prime_comparison_353.png", dpi=120)
    print("\nGraph saved as prime_comparison_353.png")
    plt.show()

main_353()
