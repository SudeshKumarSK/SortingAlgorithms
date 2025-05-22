# Implementation of insertion sort technique in python from scratch

from typing import List

# Function Definition of insertion sort. It sorts the integer array in-place.
def insertion_sort(arr: List[int], ascending=True) -> None:
    n = len(arr)

    for i in range(1, n):
        # We loop from i to "one index before the first element" backwards.
        # If they are in the right order we just insert them into our sorted region. - break the loop
        # If not we swap until we know that element is in the sorted region.
        for j in range(i, 0, -1):
            if ascending:
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]

                else:
                    break

            else:
                if arr[j - 1] < arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]

                else:
                    break



if __name__ == "__main__":
    nums = [-5, 3, 2, 1, -3, 4, -2, 7, 2, 2]
    print(f"Before sorting the integer array: {nums}")
    insertion_sort(nums)
    print(f"After sorting the integer array in Ascending Order: {nums}")
    print()

    nums = [-5, 3, 2, 1, -3, 4, -2, 7, 2, 2]
    print(f"Before sorting the integer array: {nums}")
    insertion_sort(nums, ascending=False)
    print(f"After sorting the integer array in Descending Order: {nums}")
    print()