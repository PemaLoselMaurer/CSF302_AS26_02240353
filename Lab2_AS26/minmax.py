import random
import sys

sys.setrecursionlimit(10000)

count_353 = 0

def minmax_353(A_353, lo_353, hi_353):
    global count_353

    if lo_353 == hi_353:
        return A_353[lo_353], A_353[lo_353]

    if hi_353 == lo_353 + 1:
        count_353 += 1
        if A_353[lo_353] < A_353[hi_353]:
            return A_353[lo_353], A_353[hi_353]
        return A_353[hi_353], A_353[lo_353]

    mid_353 = (lo_353 + hi_353) // 2
    min1_353, max1_353 = minmax_353(A_353, lo_353, mid_353)
    min2_353, max2_353 = minmax_353(A_353, mid_353 + 1, hi_353)

    count_353 += 1
    small_353 = min2_353 if min2_353 < min1_353 else min1_353
    count_353 += 1
    large_353 = max2_353 if max2_353 > max1_353 else max1_353

    return small_353, large_353

def predicted_353(n_353):
    return 3 * n_353 // 2 - 2

print("%-8s %-14s %-14s %-14s %s" % ("n", "Measured", "Predicted", "2n-2", "min/max OK"))
for n_353 in [8, 64, 512, 4096]:
    A_353 = [random.randint(-10000, 10000) for _ in range(n_353)]
    count_353 = 0
    lo_val_353, hi_val_353 = minmax_353(A_353, 0, n_353 - 1)
    ok_353 = (lo_val_353 == min(A_353)) and (hi_val_353 == max(A_353))
    print("%-8d %-14d %-14d %-14d %s" % (
        n_353, count_353, predicted_353(n_353), 2 * n_353 - 2, ok_353))
