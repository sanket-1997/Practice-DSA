def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Merge the two sorted halves
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy remaining elements
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    # ⚠️ Copy merged elements back to arr
    for i in range(len(temp)):
        arr[low + i] = temp[i]


# Example usage
arr = [10, 2, 4, 2, 5, 6, 1, 7]
print("Before sorting:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)
