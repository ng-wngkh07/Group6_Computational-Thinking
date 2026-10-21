def binary_search(a: list[int], key: int) -> int:
    """
    Binary search for key in sorted list a.

    Difference from C++:
    In Python, integers have arbitrary precision and do not overflow when computing
    mid. Python uses len(a) instead of a.size(), and // for integer division.
    """
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 5))
    print(binary_search([1, 3, 5, 7, 9], 1))
    print(binary_search([1, 3, 5, 7, 9], 9))
    print(binary_search([1, 3, 5, 7, 9], 4))
    print(binary_search([], 5))
