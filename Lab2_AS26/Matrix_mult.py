import random

mult_353 = 0
add_353 = 0

def is_power_of_two_353(n_353):
    if n_353 < 2:
        return False
    while n_353 % 2 == 0:
        n_353 = n_353 // 2
    return n_353 == 1

def multiply_353(a_353, b_353, n_353):
    global mult_353, add_353

    mult_353 = 0
    add_353 = 0

    c_353 = [[0] * n_353 for _ in range(n_353)]

    for i_353 in range(n_353):
        for j_353 in range(n_353):
            total_353 = 0
            for k_353 in range(n_353):
                total_353 = total_353 + a_353[i_353][k_353] * b_353[k_353][j_353]
                mult_353 += 1
                add_353 += 1
            c_353[i_353][j_353] = total_353

    return c_353

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
    print("\nMatrix " + name_353 + ":")
    for row_353 in matrix_353:
        print("  " + "  ".join(str(value_353).rjust(5) for value_353 in row_353))

def main_353():
    print("===== SQUARE MATRIX MULTIPLICATION (353) =====")

    while True:
        n_353 = int(input("Enter matrix size n (power of 2: 2, 4, 8, 16 ...): "))
        if is_power_of_two_353(n_353):
            break
        print(str(n_353) + " is not a power of 2. Try again.")

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

    c_353 = multiply_353(a_353, b_353, n_353)
    display_353(c_353, "C = A x B")

    total_353 = mult_353 + add_353
    print("\n---------- Step / Frequency Count ----------")
    print("Matrix size n            : " + str(n_353))
    print("Multiplications          : " + str(mult_353) + "   ( = n^3 )")
    print("Additions                : " + str(add_353) + "   ( = n^3 )")
    print("Total basic operations   : " + str(total_353) + "   ( = 2 * n^3 )")
    print("n^3 for this n           : " + str(n_353 ** 3))
    print("Time complexity          : O(n^3)")
    print("--------------------------------------------")

main_353()
