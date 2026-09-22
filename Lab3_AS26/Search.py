import math
import random
import matplotlib.pyplot as plt

def binary_search_353(arr_353, key_353):
    comparisons_353 = 0
    iterations_353 = 0

    low_353 = 0
    high_353 = len(arr_353) - 1

    while low_353 <= high_353:
        iterations_353 += 1
        mid_353 = (low_353 + high_353) // 2

        comparisons_353 += 1
        if arr_353[mid_353] == key_353:
            return mid_353, comparisons_353, iterations_353

        if arr_353[mid_353] < key_353:
            low_353 = mid_353 + 1
        else:
            high_353 = mid_353 - 1

    return -1, comparisons_353, iterations_353

def ternary_search_353(arr_353, key_353):
    comparisons_353 = 0
    iterations_353 = 0

    low_353 = 0
    high_353 = len(arr_353) - 1

    while low_353 <= high_353:
        iterations_353 += 1
        third_353 = (high_353 - low_353) // 3
        mid1_353 = low_353 + third_353
        mid2_353 = high_353 - third_353

        comparisons_353 += 1
        if arr_353[mid1_353] == key_353:
            return mid1_353, comparisons_353, iterations_353

        comparisons_353 += 1
        if arr_353[mid2_353] == key_353:
            return mid2_353, comparisons_353, iterations_353

        if key_353 < arr_353[mid1_353]:
            high_353 = mid1_353 - 1
        elif key_353 > arr_353[mid2_353]:
            low_353 = mid2_353 + 1
        else:
            low_353 = mid1_353 + 1
            high_353 = mid2_353 - 1

    return -1, comparisons_353, iterations_353

def generate_array_353(n_353):
    return sorted(random.sample(range(1, n_353 * 10 + 1), n_353))

def report_353(name_353, index_353, comparisons_353, iterations_353):
    if index_353 == -1:
        print(name_353 + " : key NOT found")
    else:
        print(name_353 + " : key found at index " + str(index_353))
    print("    comparisons : " + str(comparisons_353))
    print("    iterations  : " + str(iterations_353))

def search_353(arr_353, which_353):
    if not arr_353:
        print("Array is empty. Use option 1 first.")
        return

    key_353 = int(input("Enter the key to search: "))

    if which_353 == "binary":
        index_353, comparisons_353, iterations_353 = binary_search_353(arr_353, key_353)
        report_353("Binary Search", index_353, comparisons_353, iterations_353)
    else:
        index_353, comparisons_353, iterations_353 = ternary_search_353(arr_353, key_353)
        report_353("Ternary Search", index_353, comparisons_353, iterations_353)

def best_case_353(arr_353):
    if not arr_353:
        print("Array is empty. Use option 1 first.")
        return

    n_353 = len(arr_353)

    # binary search looks at the middle element first
    key_b_353 = arr_353[(n_353 - 1) // 2]
    # ternary search looks at the first one-third point first
    key_t_353 = arr_353[(n_353 - 1) // 3]

    b_353 = binary_search_353(arr_353, key_b_353)
    t_353 = ternary_search_353(arr_353, key_t_353)

    print("\n---------- BEST CASE (key present, fewest comparisons) ----------")
    print("Array size n : " + str(n_353))
    print("\nBinary  : key = " + str(key_b_353) + " (the middle element)")
    report_353("Binary Search", b_353[0], b_353[1], b_353[2])
    print("\nTernary : key = " + str(key_t_353) + " (the first one-third point)")
    report_353("Ternary Search", t_353[0], t_353[1], t_353[2])
    print("\nBoth find the key in the very first iteration, so the best case")
    print("is O(1) for both methods.")

def worst_case_353(arr_353):
    if not arr_353:
        print("Array is empty. Use option 1 first.")
        return

    n_353 = len(arr_353)
    key_353 = arr_353[-1] + 1          # a value that is certainly absent

    b_353 = binary_search_353(arr_353, key_353)
    t_353 = ternary_search_353(arr_353, key_353)

    print("\n---------- WORST CASE (key absent, search runs to the end) ----------")
    print("Array size n : " + str(n_353))
    print("Key searched : " + str(key_353) + "  (not in the array)")
    report_353("\nBinary Search", b_353[0], b_353[1], b_353[2])
    report_353("\nTernary Search", t_353[0], t_353[1], t_353[2])

    print("\nExpected from the recurrences:")
    print("    Binary  T(n) = T(n/2) + O(1)  ->  about log2(n) = "
          + str(round(math.log2(n_353), 2)) + " iterations, 1 comparison each")
    print("    Ternary T(n) = T(n/3) + O(1)  ->  about log3(n) = "
          + str(round(math.log(n_353, 3), 2)) + " iterations, 2 comparisons each")

def compare_table_353():
    sizes_353 = [100, 500, 1000, 5000, 10000, 50000, 100000]

    bin_comp_353 = []
    ter_comp_353 = []
    bin_iter_353 = []
    ter_iter_353 = []

    print("\nStep / Frequency Count Table (worst case : key absent)")
    print("-" * 86)
    print(f"{'n':>8}{'Bin comps':>12}{'Ter comps':>12}{'Bin iters':>12}"
          f"{'Ter iters':>12}{'log2 n':>10}{'2*log3 n':>12}")
    print("-" * 86)

    for n_353 in sizes_353:
        arr_353 = generate_array_353(n_353)
        key_353 = arr_353[-1] + 1

        b_353 = binary_search_353(arr_353, key_353)
        t_353 = ternary_search_353(arr_353, key_353)

        bin_comp_353.append(b_353[1])
        ter_comp_353.append(t_353[1])
        bin_iter_353.append(b_353[2])
        ter_iter_353.append(t_353[2])

        print(f"{n_353:>8}{b_353[1]:>12}{t_353[1]:>12}{b_353[2]:>12}{t_353[2]:>12}"
              f"{math.log2(n_353):>10.2f}{2 * math.log(n_353, 3):>12.2f}")

    print("-" * 86)
    print("Ternary search needs FEWER iterations (log3 n < log2 n) but TWO")
    print("comparisons in each iteration, so its total comparison count")
    print("2*log3(n) = 1.26*log2(n) is always higher than binary search's log2(n).")

    plot_graph_353(sizes_353, bin_comp_353, ter_comp_353, bin_iter_353, ter_iter_353)

def plot_graph_353(sizes_353, bin_comp_353, ter_comp_353, bin_iter_353, ter_iter_353):
    fig_353, ax_353 = plt.subplots(1, 2, figsize=(12, 5))

    ax_353[0].plot(sizes_353, bin_comp_353, "o-", color="crimson", label="Binary  log2 n")
    ax_353[0].plot(sizes_353, ter_comp_353, "s-", color="seagreen", label="Ternary  2*log3 n")
    ax_353[0].set_title("Comparisons in the worst case")
    ax_353[0].set_xlabel("Array size n")
    ax_353[0].set_ylabel("Number of comparisons")
    ax_353[0].set_xscale("log")
    ax_353[0].legend()
    ax_353[0].grid(True, alpha=0.3)

    ax_353[1].plot(sizes_353, bin_iter_353, "o-", color="crimson", label="Binary  T(n)=T(n/2)+O(1)")
    ax_353[1].plot(sizes_353, ter_iter_353, "s-", color="seagreen", label="Ternary  T(n)=T(n/3)+O(1)")
    ax_353[1].set_title("Iterations (recursion depth) in the worst case")
    ax_353[1].set_xlabel("Array size n")
    ax_353[1].set_ylabel("Number of iterations")
    ax_353[1].set_xscale("log")
    ax_353[1].legend()
    ax_353[1].grid(True, alpha=0.3)

    fig_353.suptitle("Binary Search vs Ternary Search (353)")
    fig_353.tight_layout()
    fig_353.savefig("search_comparison_353.png", dpi=120)
    print("\nGraph saved as search_comparison_353.png")
    plt.show()

def show_menu_353():
    print("\n========== BINARY SEARCH vs TERNARY SEARCH (353) ==========")
    print("1. Generate n sorted random numbers -> Array")
    print("2. Display Array")
    print("3. Search for a key using Binary Search")
    print("4. Search for a key using Ternary Search")
    print("5. Step / frequency count for BEST case")
    print("6. Step / frequency count for WORST case")
    print("7. Step / frequency count comparison table and graph")
    print("0. Exit")
    print("===========================================================")

def main_353():
    array_353 = []

    while True:
        show_menu_353()
        choice_353 = input("Enter your choice: ").strip()

        if choice_353 == "1":
            n_353 = int(input("How many numbers? "))
            array_353 = generate_array_353(n_353)
            print(str(n_353) + " sorted random numbers generated.")

        elif choice_353 == "2":
            if not array_353:
                print("Array is empty. Use option 1 first.")
            else:
                print("Array (" + str(len(array_353)) + " elements):")
                if len(array_353) > 100:
                    print(array_353[:50])
                    print("... (" + str(len(array_353) - 100) + " more) ...")
                    print(array_353[-50:])
                else:
                    print(array_353)

        elif choice_353 == "3":
            search_353(array_353, "binary")

        elif choice_353 == "4":
            search_353(array_353, "ternary")

        elif choice_353 == "5":
            best_case_353(array_353)

        elif choice_353 == "6":
            worst_case_353(array_353)

        elif choice_353 == "7":
            compare_table_353()

        elif choice_353 == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice, try again.")

main_353()

# ---------------------------------------------------------------------------
# ANALYSIS / CONCLUSION
#
#   Binary   T(n) = T(n/2) + O(1)  ->  O(log2 n), 1 comparison per level
#   Ternary  T(n) = T(n/3) + O(1)  ->  O(log3 n), 2 comparisons per level
#   Best case is O(1) for both.
#
# Observed worst case (key absent):
#       n         Bin comps   Ter comps   Bin iters   Ter iters
#       1000            10          12          10           6
#      10000            14          18          14           9
#     100000            17          22          17          11
#
# The counts match the recurrences: ternary needs about 37 % fewer iterations
# but 2*log3(n) = 1.26*log2(n) comparisons, i.e. 26 % more work.  In general a
# k-way split costs (k-1)*log(n)/log(k) comparisons, which is smallest at
# k = 2, so binary search is the better choice.
# ---------------------------------------------------------------------------
