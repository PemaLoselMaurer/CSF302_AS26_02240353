import random
import time

steps_353 = 0

def merge_sort_353(arr_353):
    global steps_353

    if len(arr_353) <= 1:
        return arr_353

    mid_353 = len(arr_353) // 2
    left_353 = merge_sort_353(arr_353[:mid_353])
    right_353 = merge_sort_353(arr_353[mid_353:])

    return merge_353(left_353, right_353)

def merge_353(left_353, right_353):
    global steps_353

    merged_353 = []
    i_353 = 0
    j_353 = 0

    while i_353 < len(left_353) and j_353 < len(right_353):
        steps_353 += 1
        if left_353[i_353] <= right_353[j_353]:
            merged_353.append(left_353[i_353])
            i_353 += 1
        else:
            merged_353.append(right_353[j_353])
            j_353 += 1

    while i_353 < len(left_353):
        steps_353 += 1
        merged_353.append(left_353[i_353])
        i_353 += 1

    while j_353 < len(right_353):
        steps_353 += 1
        merged_353.append(right_353[j_353])
        j_353 += 1

    return merged_353

def bubble_sort_desc_353(arr_353):
    copy_353 = arr_353[:]
    count_353 = 0
    n_353 = len(copy_353)

    for i_353 in range(n_353 - 1):
        swapped_353 = False
        for j_353 in range(n_353 - 1 - i_353):
            count_353 += 1
            if copy_353[j_353] < copy_353[j_353 + 1]:
                copy_353[j_353], copy_353[j_353 + 1] = copy_353[j_353 + 1], copy_353[j_353]
                swapped_353 = True
        if not swapped_353:
            break

    return copy_353, count_353

def run_merge_sort_353(arr_353):
    global steps_353

    steps_353 = 0
    start_353 = time.perf_counter()
    sorted_353 = merge_sort_353(arr_353)
    end_353 = time.perf_counter()
    milli_sec_353 = (end_353 - start_353) * 1000

    return sorted_353, steps_353, milli_sec_353

def make_data_353(size_353, kind_353):
    if kind_353 == "random":
        return [random.randint(1, 10000) for _ in range(size_353)]
    if kind_353 == "sorted":
        return list(range(size_353))
    if kind_353 == "reverse":
        return list(range(size_353, 0, -1))
    return []

def analyse_353(kind_353, title_353):
    sizes_353 = [100, 200, 400, 800, 1600, 3200]

    print("\nMerge Sort on " + title_353)
    print("-" * 52)
    print(f"{'n':>6} {'Steps':>10} {'n log2 n':>12} {'Time (ms)':>12}")
    print("-" * 52)

    for n_353 in sizes_353:
        data_353 = make_data_353(n_353, kind_353)
        _, count_353, ms_353 = run_merge_sort_353(data_353)

        nlogn_353 = n_353 * (len(bin(n_353)) - 3)
        print(f"{n_353:>6} {count_353:>10} {nlogn_353:>12} {ms_353:>12.3f}")

    print("-" * 52)
    print("Steps stay close to n log2 n  ->  time complexity is O(n log n)")

def show_menu_353():
    print("\n========== MERGE SORT ANALYSIS (353) ==========")
    print("1. Generate n random numbers -> Array")
    print("2. Display Array")
    print("3. Sort in Ascending Order using Merge Sort")
    print("4. Sort in Descending Order using Bubble Sort")
    print("5. Time Complexity for random data")
    print("6. Time Complexity for already sorted data")
    print("7. Time Complexity for descending sorted data")
    print("0. Exit")
    print("===============================================")

def main_353():
    array_353 = []

    while True:
        show_menu_353()
        choice_353 = input("Enter your choice: ").strip()

        if choice_353 == "1":
            n_353 = int(input("How many numbers? "))
            array_353 = [random.randint(1, 1000) for _ in range(n_353)]
            print(str(n_353) + " random numbers generated.")

        elif choice_353 == "2":
            if not array_353:
                print("Array is empty. Use option 1 first.")
            else:
                print("Array (" + str(len(array_353)) + " elements):")
                print(array_353)

        elif choice_353 == "3":
            if not array_353:
                print("Array is empty. Use option 1 first.")
            else:
                result_353, count_353, ms_353 = run_merge_sort_353(array_353)
                array_353 = result_353
                print("Sorted in ascending order (Merge Sort):")
                print(array_353)
                print("Step count : " + str(count_353))
                print("Time taken : " + format(ms_353, ".3f") + " ms")

        elif choice_353 == "4":
            if not array_353:
                print("Array is empty. Use option 1 first.")
            else:
                result_353, count_353 = bubble_sort_desc_353(array_353)
                array_353 = result_353
                print("Sorted in descending order (Bubble Sort):")
                print(array_353)
                print("Step count : " + str(count_353))

        elif choice_353 == "5":
            analyse_353("random", "Random data")

        elif choice_353 == "6":
            analyse_353("sorted", "Sorted data")

        elif choice_353 == "7":
            analyse_353("reverse", "Reverse data")

        elif choice_353 == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice, try again.")

main_353()
