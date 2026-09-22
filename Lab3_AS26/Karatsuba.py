import random
import time
import matplotlib.pyplot as plt

trad_mult_353 = 0
trad_add_353 = 0
kara_mult_353 = 0
kara_add_353 = 0

def strip_353(x_353):
    x_353 = x_353.lstrip("0")
    if x_353 == "":
        return "0"
    return x_353

def add_353(x_353, y_353):
    global kara_add_353

    n_353 = max(len(x_353), len(y_353))
    x_353 = x_353.zfill(n_353)
    y_353 = y_353.zfill(n_353)

    result_353 = []
    carry_353 = 0

    for i_353 in range(n_353 - 1, -1, -1):
        total_353 = int(x_353[i_353]) + int(y_353[i_353]) + carry_353
        kara_add_353 += 1
        result_353.append(str(total_353 % 10))
        carry_353 = total_353 // 10

    if carry_353 > 0:
        result_353.append(str(carry_353))

    return strip_353("".join(reversed(result_353)))

def sub_353(x_353, y_353):
    global kara_add_353

    n_353 = max(len(x_353), len(y_353))
    x_353 = x_353.zfill(n_353)
    y_353 = y_353.zfill(n_353)

    result_353 = []
    borrow_353 = 0

    for i_353 in range(n_353 - 1, -1, -1):
        diff_353 = int(x_353[i_353]) - int(y_353[i_353]) - borrow_353
        kara_add_353 += 1
        if diff_353 < 0:
            diff_353 += 10
            borrow_353 = 1
        else:
            borrow_353 = 0
        result_353.append(str(diff_353))

    return strip_353("".join(reversed(result_353)))

def shift_353(x_353, places_353):
    if x_353 == "0":
        return "0"
    return x_353 + "0" * places_353

def next_power_of_two_353(n_353):
    size_353 = 1
    while size_353 < n_353:
        size_353 = size_353 * 2
    return size_353

def pad_353(x_353, y_353):
    size_353 = next_power_of_two_353(max(len(x_353), len(y_353)))
    return x_353.zfill(size_353), y_353.zfill(size_353)

def traditional_353(x_353, y_353):
    global trad_mult_353, trad_add_353

    n_353 = len(x_353)
    m_353 = len(y_353)
    result_353 = [0] * (n_353 + m_353)

    for i_353 in range(n_353 - 1, -1, -1):
        for j_353 in range(m_353 - 1, -1, -1):
            result_353[i_353 + j_353 + 1] += int(x_353[i_353]) * int(y_353[j_353])
            trad_mult_353 += 1
            trad_add_353 += 1

    for k_353 in range(len(result_353) - 1, 0, -1):
        carry_353 = result_353[k_353] // 10
        result_353[k_353] = result_353[k_353] % 10
        result_353[k_353 - 1] += carry_353
        trad_add_353 += 1

    return strip_353("".join(str(d_353) for d_353 in result_353))

def karatsuba_353(x_353, y_353):
    global kara_mult_353

    n_353 = len(x_353)

    if n_353 == 1:
        kara_mult_353 += 1
        return str(int(x_353) * int(y_353))

    half_353 = n_353 // 2
    x_hi_353 = x_353[:half_353]
    x_lo_353 = x_353[half_353:]
    y_hi_353 = y_353[:half_353]
    y_lo_353 = y_353[half_353:]

    # 3 recursive multiplications instead of the usual 4
    z2_353 = karatsuba_353(x_hi_353, y_hi_353)
    z0_353 = karatsuba_353(x_lo_353, y_lo_353)

    sum_x_353 = add_353(x_hi_353, x_lo_353)
    sum_y_353 = add_353(y_hi_353, y_lo_353)

    if len(sum_x_353) > half_353:
        carry_x_353 = 1
        rest_x_353 = sum_x_353[1:]
    else:
        carry_x_353 = 0
        rest_x_353 = sum_x_353.zfill(half_353)

    if len(sum_y_353) > half_353:
        carry_y_353 = 1
        rest_y_353 = sum_y_353[1:]
    else:
        carry_y_353 = 0
        rest_y_353 = sum_y_353.zfill(half_353)

    middle_353 = karatsuba_353(rest_x_353, rest_y_353)

    if carry_x_353 == 1:
        middle_353 = add_353(middle_353, shift_353(strip_353(rest_y_353), half_353))
    if carry_y_353 == 1:
        middle_353 = add_353(middle_353, shift_353(strip_353(rest_x_353), half_353))
    if carry_x_353 == 1 and carry_y_353 == 1:
        middle_353 = add_353(middle_353, shift_353("1", 2 * half_353))

    z1_353 = sub_353(middle_353, add_353(z2_353, z0_353))

    total_353 = add_353(shift_353(z2_353, 2 * half_353), shift_353(z1_353, half_353))
    return add_353(total_353, z0_353)

def run_traditional_353(x_353, y_353):
    global trad_mult_353, trad_add_353

    trad_mult_353 = 0
    trad_add_353 = 0

    start_353 = time.perf_counter()
    result_353 = traditional_353(x_353, y_353)
    end_353 = time.perf_counter()

    return result_353, (end_353 - start_353) * 1000

def run_karatsuba_353(x_353, y_353):
    global kara_mult_353, kara_add_353

    kara_mult_353 = 0
    kara_add_353 = 0

    start_353 = time.perf_counter()
    result_353 = karatsuba_353(x_353, y_353)
    end_353 = time.perf_counter()

    return result_353, (end_353 - start_353) * 1000

def random_number_353(digits_353):
    number_353 = str(random.randint(1, 9))
    number_353 += "".join(str(random.randint(0, 9)) for _ in range(digits_353 - 1))
    return number_353

def manual_number_353(name_353):
    while True:
        value_353 = input("Enter number " + name_353 + " : ").strip()
        if value_353.isdigit():
            return strip_353(value_353)
        print("Digits only, please.")

def display_353(number_353, name_353):
    print("\n" + name_353 + "  (" + str(len(number_353)) + " digits):")
    if len(number_353) > 120:
        print("  " + number_353[:60] + " ... " + number_353[-60:])
    else:
        print("  " + number_353)

def multiply_and_verify_353():
    print("\n1. Generate numbers randomly")
    print("2. Enter numbers manually")
    choice_353 = input("Enter your choice: ").strip()

    if choice_353 == "2":
        x_353 = manual_number_353("A")
        y_353 = manual_number_353("B")
    else:
        digits_353 = int(input("How many digits (8, 16, 32, ... 1024): "))
        x_353 = random_number_353(digits_353)
        y_353 = random_number_353(digits_353)
        print("Random numbers generated.")

    display_353(x_353, "Number A")
    display_353(y_353, "Number B")

    x_pad_353, y_pad_353 = pad_353(x_353, y_353)
    print("\nPadded to " + str(len(x_pad_353)) + " digits (next power of 2) for the split.")

    p1_353, time1_353 = run_traditional_353(x_pad_353, y_pad_353)
    p2_353, time2_353 = run_karatsuba_353(x_pad_353, y_pad_353)

    display_353(p1_353, "Product (Traditional)")
    display_353(p2_353, "Product (Karatsuba)")

    n_353 = len(x_pad_353)
    print("\n---------- Step / Frequency Count for n = " + str(n_353) + " digits ----------")
    print(f"{'Method':<14}{'Digit mults':>14}{'Digit add/sub':>16}{'Time (ms)':>13}")
    print("-" * 57)
    print(f"{'Traditional':<14}{trad_mult_353:>14}{trad_add_353:>16}{time1_353:>13.3f}")
    print(f"{'Karatsuba':<14}{kara_mult_353:>14}{kara_add_353:>16}{time2_353:>13.3f}")
    print("-" * 57)
    print("Traditional mults = n^2        = " + str(n_353 ** 2))
    print("Karatsuba   mults = 3^log2(n)  = " + str(3 ** (len(bin(n_353)) - 3)))

    if p1_353 == p2_353:
        print("\nVERIFIED : both methods produced the SAME product.")
    else:
        print("\nMISMATCH : the two products are different.")

    if p2_353 == str(int(x_353) * int(y_353)):
        print("CROSS CHECK : product also matches Python's built-in multiplication.")
    else:
        print("CROSS CHECK : product does NOT match Python's built-in multiplication.")

def analyse_353():
    sizes_353 = [8, 16, 32, 64, 128, 256, 512, 1024]

    trad_m_353 = []
    kara_m_353 = []
    trad_t_353 = []
    kara_t_353 = []

    print("\nStep / Frequency Count Table : Traditional vs Karatsuba")
    print("-" * 80)
    print(f"{'digits':>7}{'Trad mults':>13}{'Kara mults':>13}"
          f"{'Trad (ms)':>13}{'Kara (ms)':>13}{'Match':>8}")
    print("-" * 80)

    for n_353 in sizes_353:
        x_353 = random_number_353(n_353)
        y_353 = random_number_353(n_353)
        x_pad_353, y_pad_353 = pad_353(x_353, y_353)

        p1_353, time1_353 = run_traditional_353(x_pad_353, y_pad_353)
        p2_353, time2_353 = run_karatsuba_353(x_pad_353, y_pad_353)

        trad_m_353.append(trad_mult_353)
        kara_m_353.append(kara_mult_353)
        trad_t_353.append(time1_353)
        kara_t_353.append(time2_353)

        ok_353 = (p1_353 == p2_353 and p1_353 == str(int(x_353) * int(y_353)))
        print(f"{n_353:>7}{trad_mult_353:>13}{kara_mult_353:>13}"
              f"{time1_353:>13.3f}{time2_353:>13.3f}{('yes' if ok_353 else 'NO'):>8}")

    print("-" * 80)
    print("Traditional : n^2       digit multiplications  ->  O(n^2)")
    print("Karatsuba   : 3^log2(n) digit multiplications  ->  O(n^1.585)")

    plot_graph_353(sizes_353, trad_m_353, kara_m_353, trad_t_353, kara_t_353)

def plot_graph_353(sizes_353, trad_m_353, kara_m_353, trad_t_353, kara_t_353):
    fig_353, ax_353 = plt.subplots(1, 2, figsize=(12, 5))

    ax_353[0].plot(sizes_353, trad_m_353, "o-", color="crimson", label="Traditional  n^2")
    ax_353[0].plot(sizes_353, kara_m_353, "s-", color="seagreen", label="Karatsuba  n^1.585")
    ax_353[0].set_title("Single digit multiplication count")
    ax_353[0].set_xlabel("Number of digits n")
    ax_353[0].set_ylabel("Multiplications (log scale)")
    ax_353[0].set_xscale("log", base=2)
    ax_353[0].set_yscale("log")
    ax_353[0].legend()
    ax_353[0].grid(True, alpha=0.3)

    ax_353[1].plot(sizes_353, trad_t_353, "o-", color="crimson", label="Traditional")
    ax_353[1].plot(sizes_353, kara_t_353, "s-", color="seagreen", label="Karatsuba")
    ax_353[1].set_title("Running time")
    ax_353[1].set_xlabel("Number of digits n")
    ax_353[1].set_ylabel("Time in ms (log scale)")
    ax_353[1].set_xscale("log", base=2)
    ax_353[1].set_yscale("log")
    ax_353[1].legend()
    ax_353[1].grid(True, alpha=0.3)

    fig_353.suptitle("Large Integer Multiplication: Traditional vs Karatsuba (353)")
    fig_353.tight_layout()
    fig_353.savefig("karatsuba_comparison_353.png", dpi=120)
    print("\nGraph saved as karatsuba_comparison_353.png")
    plt.show()

def show_menu_353():
    print("\n===== LARGE INTEGER MULTIPLICATION : TRADITIONAL vs KARATSUBA (353) =====")
    print("1. Multiply two numbers by both methods and verify")
    print("2. Step / frequency count table and graph (8 to 1024 digits)")
    print("0. Exit")
    print("=========================================================================")

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
# ANALYSIS
#
#   Traditional  two nested loops over the digits  ->  O(n^2)
#   Karatsuba    T(n) = 3 T(n/2) + O(n)  ->  O(n^log2(3)) = O(n^1.585)
#                (Master Theorem case 1, since log2(3) = 1.585 > 1)
#
# Observed digit multiplication counts:
#       digits      n^2       3^log2(n)
#          16       256           81
#         128     16384         2187
#        1024   1048576        59049
#   At 1024 digits Karatsuba uses about 5.6 % of the multiplications.
#
# Observed running time (ms):
#       digits      Trad     Kara    ratio Trad/Kara
#           64      0.59     4.16       0.14
#          256      7.95    34.27       0.23
#         1024    140.94   295.16       0.48
#
#   The traditional method is still faster at every size tested, but the ratio
#   multiplies by about 1.5 on each doubling of n, putting the cross-over near
#   4000 digits here.  A digit multiplication in Python costs no more than a
#   digit addition, so the recursion, string slicing and three O(n) additions
#   per split outweigh the multiplication saved until n is large.
# ---------------------------------------------------------------------------
# CONCLUSION
#
# Both methods give the same product, and the counts confirm the O(n^2) and
# O(n^1.585) growth rates.  The asymptotic gain of Karatsuba is real but only
# pays off past a cutoff, which is why real libraries fall back to
# grade-school multiplication for short numbers and switch to Karatsuba only
# for long ones.
# ---------------------------------------------------------------------------
