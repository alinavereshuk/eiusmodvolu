def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = [11, 12, 22, 25, 34, 64, 90]
index = binary_search(arr, 25)
print("Index of 25 using Binary Search:", index)
