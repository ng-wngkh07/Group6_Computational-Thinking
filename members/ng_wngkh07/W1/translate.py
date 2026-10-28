def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted ranges into the original list."""
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + 1]
    i = 0  
    j = 0 
    k = left 
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1 
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1
    while i < len(L):
        arr[k] = L[i]
        i = i + 1
        k = k + 1
    while j < len(R):
        arr[k] = R[j]
        j = j + 1
        k = k + 1

def merge_sort(arr: list[int], left: int, right: int) -> None:
    """Sort a selected list range using merge sort."""
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)