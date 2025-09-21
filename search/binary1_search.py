def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Binary Search Iterative (6):", binary_search_iterative(arr, 6))
