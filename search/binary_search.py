def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Binary Search Recursive (5):", binary_search_recursive(arr, 5, 0, len(arr) - 1))
