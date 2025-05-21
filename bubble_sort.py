# Bubble Sort Algorithm Implementation from Scratch
from typing import List

# Method to sort a given integer list in-place.
def bubble_sort(arr: List[int], ascending: bool =True) -> None:
    # Time Complexity -> O(n^2)
    # Space Complexity -> O(1)

    n = len(arr)
    not_sorted = True
    
    # Ascending Order
    if ascending:
        while not_sorted:
            not_sorted = False
            for i in range(1, n):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    not_sorted = True

    # Descending Order
    else:
        while not_sorted:
            not_sorted = False
            for i in range(1, n):
                if arr[i] > arr[i - 1]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    not_sorted = True



if __name__ == "__main__":
    nums = [-5, 3, 2, -1, 2, 2, 0, 7]
    print(f"Before sorting the integer array: {nums}")
    bubble_sort(nums)
    print(f"After sorting the integer array in Ascending Order: {nums}")
    print()

    nums = [-5, 3, 2, -1, 2, 2, 0, 7]
    print(f"Before sorting the integer array: {nums}")
    bubble_sort(nums, ascending=False)
    print(f"After sorting the integer array in Descending Order: {nums}")
