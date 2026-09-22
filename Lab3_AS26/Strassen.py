import random
import time
import matplotlib.pyplot as plt

trad_mult_353 = 0
trad_add_353 = 0
stras_mult_353 = 0
stras_add_353 = 0

def is_power_of_two_353(n_353):
    if n_353 < 1:
        return False
    while n_353 % 2 == 0:
        n_353 = n_353 // 2
    return n_353 == 1

def log2_353(n_353):
    return len(bin(n_353)) - 3

def traditional_353(a_353, b_353, n_353):
    global trad_mult_353, trad_add_353

    c_353 = [[0] * n_353 for _ in range(n_353)]

    for i_353 in range(n_353):
        for j_353 in range(n_353):
            total_353 = 0
            for k_353 in range(n_353):
                total_353 = total_353 + a_353[i_353][k_353] * b_353[k_353][j_353]
                trad_mult_353 += 1
                trad_add_353 += 1
            c_353[i_353][j_353] = total_353

    return c_353

def add_matrix_353(a_353, b_353):
    global stras_add_353

    n_353 = len(a_353)
    stras_add_353 += n_353 * n_353

    return [[a_353[i_353][j_353] + b_353[i_353][j_353] for j_353 in range(n_353)]
            for i_353 in range(n_353)]

def sub_matrix_353(a_353, b_353):
    global stras_add_353

    n_353 = len(a_353)
    stras_add_353 += n_353 * n_353

    return [[a_353[i_353][j_353] - b_353[i_353][j_353] for j_353 in range(n_353)]
            for i_353 in range(n_353)]

def split_353(matrix_353):
    half_353 = len(matrix_353) // 2

    a11_353 = [row_353[:half_353] for row_353 in matrix_353[:half_353]]
    a12_353 = [row_353[half_353:] for row_353 in matrix_353[:half_353]]
    a21_353 = [row_353[:half_353] for row_353 in matrix_353[half_353:]]
    a22_353 = [row_353[half_353:] for row_353 in matrix_353[half_353:]]

    return a11_353, a12_353, a21_353, a22_353

def join_353(c11_353, c12_353, c21_353, c22_353):
    top_353 = [c11_353[i_353] + c12_353[i_353] for i_353 in range(len(c11_353))]
    bottom_353 = [c21_353[i_353] + c22_353[i_353] for i_353 in range(len(c21_353))]

    return top_353 + bottom_353

def strassen_353(a_353, b_353):
    global stras_mult_353

    n_353 = len(a_353)

    if n_353 == 1:
        stras_mult_353 += 1
        return [[a_353[0][0] * b_353[0][0]]]

    a11_353, a12_353, a21_353, a22_353 = split_353(a_353)
    b11_353, b12_353, b21_353, b22_353 = split_353(b_353)

    # 7 recursive multiplications instead of the usual 8
    p1_353 = strassen_353(a11_353, sub_matrix_353(b12_353, b22_353))
    p2_353 = strassen_353(add_matrix_353(a11_353, a12_353), b22_353)
    p3_353 = strassen_353(add_matrix_353(a21_353, a22_353), b11_353)
    p4_353 = strassen_353(a22_353, sub_matrix_353(b21_353, b11_353))
    p5_353 = strassen_353(add_matrix_353(a11_353, a22_353), add_matrix_353(b11_353, b22_353))
    p6_353 = strassen_353(sub_matrix_353(a12_353, a22_353), add_matrix_353(b21_353, b22_353))
    p7_353 = strassen_353(sub_matrix_353(a11_353, a21_353), add_matrix_353(b11_353, b12_353))

    c11_353 = add_matrix_353(sub_matrix_353(add_matrix_353(p5_353, p4_353), p2_353), p6_353)
    c12_353 = add_matrix_353(p1_353, p2_353)
    c21_353 = add_matrix_353(p3_353, p4_353)
    c22_353 = sub_matrix_353(sub_matrix_353(add_matrix_353(p5_353, p1_353), p3_353), p7_353)

    return join_353(c11_353, c12_353, c21_353, c22_353)

def run_traditional_353(a_353, b_353, n_353):
    global trad_mult_353, trad_add_353

    trad_mult_353 = 0
    trad_add_353 = 0

    start_353 = time.perf_counter()
    result_353 = traditional_353(a_353, b_353, n_353)
    end_353 = time.perf_counter()

    return result_353, (end_353 - start_353) * 1000

def run_strassen_353(a_353, b_353):
    global stras_mult_353, stras_add_353

    stras_mult_353 = 0
    stras_add_353 = 0

    start_353 = time.perf_counter()
    result_353 = strassen_353(a_353, b_353)
    end_353 = time.perf_counter()

    return result_353, (end_353 - start_353) * 1000

def random_matrix_353(n_353):
    return [[random.randint(1, 9) for _ in range(n_353)] for _ in range(n_353)]

def manual_matrix_353(n_353, name_353):
    matrix_353 = []
    print("Enter matrix " + name_353 + " : " + str(n_353) +
          " numbers per row, separated by spaces")

    for i_353 in range(n_353):
        while True:
            row_353 = [int(x_353) for x_353 in input("Row " + str(i_353 + 1) + ": ").split()]
            if len(row_353) == n_353:
                break
            print("Please enter exactly " + str(n_353) + " numbers.")
        matrix_353.append(row_353)

    return matrix_353

def display_353(matrix_353, name_353):
    n_353 = len(matrix_353)

    print("\nMatrix " + name_353 + ":")
    if n_353 > 16:
        print("  (size " + str(n_353) + " x " + str(n_353) + " - too large to print)")
        return

    for row_353 in matrix_353:
        print("  " + "  ".join(str(value_353).rjust(6) for value_353 in row_353))

def read_size_353():
    while True:
        n_353 = int(input("Enter matrix size n (power of 2: 2, 4, 8, 16 ...): "))
        if is_power_of_two_353(n_353):
            return n_353
        print(str(n_353) + " is not a power of 2. Try again.")

def multiply_and_verify_353():
    n_353 = read_size_353()

    print("\n1. Generate matrices randomly")
    print("2. Enter matrices manually")
    choice_353 = input("Enter your choice: ").strip()

    if choice_353 == "2":
        a_353 = manual_matrix_353(n_353, "A")
        b_353 = manual_matrix_353(n_353, "B")
    else:
        a_353 = random_matrix_353(n_353)
        b_353 = random_matrix_353(n_353)
        print("Random matrices generated.")

    display_353(a_353, "A")
    display_353(b_353, "B")

    c1_353, time1_353 = run_traditional_353(a_353, b_353, n_353)
    c2_353, time2_353 = run_strassen_353(a_353, b_353)

    display_353(c1_353, "C = A x B  (Traditional)")
    display_353(c2_353, "C = A x B  (Strassen)")

    print("\n---------- Step / Frequency Count for n = " + str(n_353) + " ----------")
    print(f"{'Method':<14}{'Mults':>12}{'Add/Sub':>12}{'Time (ms)':>13}")
    print("-" * 51)
    print(f"{'Traditional':<14}{trad_mult_353:>12}{trad_add_353:>12}{time1_353:>13.3f}")
    print(f"{'Strassen':<14}{stras_mult_353:>12}{stras_add_353:>12}{time2_353:>13.3f}")
    print("-" * 51)
    print("Traditional mults = n^3        = " + str(n_353 ** 3))
    print("Strassen    mults = 7^log2(n)  = " + str(7 ** log2_353(n_353)))

    if c1_353 == c2_353:
        print("\nVERIFIED : both methods produced the SAME result matrix.")
    else:
        print("\nMISMATCH : the two result matrices are different.")

def analyse_353():
    sizes_353 = [2, 4, 8, 16, 32, 64, 128]

    trad_m_353 = []
    stras_m_353 = []
    trad_t_353 = []
    stras_t_353 = []

    print("\nStep / Frequency Count Table : Traditional vs Strassen")
    print("-" * 82)
    print(f"{'n':>5}{'Trad mults':>13}{'Stras mults':>13}{'Stras add/sub':>15}"
          f"{'Trad (ms)':>13}{'Stras (ms)':>13}{'Match':>8}")
    print("-" * 82)

    for n_353 in sizes_353:
        a_353 = random_matrix_353(n_353)
        b_353 = random_matrix_353(n_353)

        c1_353, time1_353 = run_traditional_353(a_353, b_353, n_353)
        c2_353, time2_353 = run_strassen_353(a_353, b_353)

        trad_m_353.append(trad_mult_353)
        stras_m_353.append(stras_mult_353)
        trad_t_353.append(time1_353)
        stras_t_353.append(time2_353)

        match_353 = "yes" if c1_353 == c2_353 else "NO"
        print(f"{n_353:>5}{trad_mult_353:>13}{stras_mult_353:>13}{stras_add_353:>15}"
              f"{time1_353:>13.3f}{time2_353:>13.3f}{match_353:>8}")

    print("-" * 82)
    print("Traditional : n^3       multiplications  ->  O(n^3)")
    print("Strassen    : 7^log2(n) multiplications  ->  O(n^2.81)")

    plot_graph_353(sizes_353, trad_m_353, stras_m_353, trad_t_353, stras_t_353)

def plot_graph_353(sizes_353, trad_m_353, stras_m_353, trad_t_353, stras_t_353):
    fig_353, ax_353 = plt.subplots(1, 2, figsize=(12, 5))

    ax_353[0].plot(sizes_353, trad_m_353, "o-", color="crimson", label="Traditional  n^3")
    ax_353[0].plot(sizes_353, stras_m_353, "s-", color="seagreen", label="Strassen  n^2.81")
    ax_353[0].set_title("Multiplication count")
    ax_353[0].set_xlabel("Matrix size n")
    ax_353[0].set_ylabel("Multiplications (log scale)")
    ax_353[0].set_xscale("log", base=2)
    ax_353[0].set_yscale("log")
    ax_353[0].legend()
    ax_353[0].grid(True, alpha=0.3)

    ax_353[1].plot(sizes_353, trad_t_353, "o-", color="crimson", label="Traditional")
    ax_353[1].plot(sizes_353, stras_t_353, "s-", color="seagreen", label="Strassen")
    ax_353[1].set_title("Running time")
    ax_353[1].set_xlabel("Matrix size n")
    ax_353[1].set_ylabel("Time in ms (log scale)")
    ax_353[1].set_xscale("log", base=2)
    ax_353[1].set_yscale("log")
    ax_353[1].legend()
    ax_353[1].grid(True, alpha=0.3)

    fig_353.suptitle("Matrix Multiplication: Traditional vs Strassen (353)")
    fig_353.tight_layout()
    fig_353.savefig("strassen_comparison_353.png", dpi=120)
    print("\nGraph saved as strassen_comparison_353.png")
    plt.show()

def show_menu_353():
    print("\n===== MATRIX MULTIPLICATION : TRADITIONAL vs STRASSEN (353) =====")
    print("1. Multiply two matrices by both methods and verify")
    print("2. Step / frequency count table and graph (n = 2 to 128)")
    print("0. Exit")
    print("=================================================================")

def main_353():
    while True:
        show_menu_353()
        choice_353 = input("Enter your choice: ").strip()

        if choice_353 == "1":
            multiply_and_verify_353()

        elif choice_353 == "2":
            analyse_353()

        elif choice_353 == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice, try again.")

main_353()

# ---------------------------------------------------------------------------
# ANALYSIS / CONCLUSION
#
#   Traditional  three nested loops  ->  O(n^3) in every case
#   Strassen     T(n) = 7 T(n/2) + O(n^2)  ->  O(n^log2(7)) = O(n^2.81)
#                (Master Theorem case 1, since log2(7) = 2.807 > 2)
#
# Observed multiplication counts:
#       n       n^3        7^log2(n)
#       8       512        343
#      32     32768      16807
#     128   2097152     823543
#   At n = 128 Strassen uses about 39 % of the multiplications.
#
# Despite that, Strassen is about 8x SLOWER in wall clock time at n = 128.
# The multiplications it saves are cheap int operations, so the 18 extra
# matrix additions per split - plus the sub-list allocation done by the
# recursion - cost more than they save.  Both methods give the same result
# matrix, but at lab sizes the constant factor decides and the traditional
# method wins; real implementations cut off the recursion (n <= 64) and
# finish with the triple loop.
# ---------------------------------------------------------------------------
