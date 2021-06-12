# https://stackoverflow.com/a/4773960

def search(arr, start, end, key):
    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == key:
        return mid

    # If arr[start...mid] is sorted
    if arr[start] <= arr[mid]:

        # As this sub-array is sorted, we can quickly
        # check if key lies in half or other half
        if arr[start] <= key <= arr[mid]:
            return search(arr, start, mid - 1, key)
        return search(arr, mid + 1, end, key)

    # If arr[start..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if arr[mid] <= key <= arr[end]:
        return search(arr, mid + 1, end, key)
    return search(arr, start, mid - 1, key)


if __name__ == "__main__":
    list_ = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    index = search(list_,0,len(list_)-1,13)
    if index != -1:
        print(f"Index: {index}")
    else:
        print("Key not found")