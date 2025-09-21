def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Linear Search (4):", linear_search(arr, 4))
