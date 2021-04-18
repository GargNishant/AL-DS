import random


def sort(arr, last_index=None):
    if last_index is None:
        last_index = len(arr)

    if last_index == 1:
        return

    for i in range(last_index-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return sort(arr, last_index=last_index-1)

if __name__ == "__main__":
    numbers = [el for el in range(10)]
    random.shuffle(numbers)
    print(numbers)
    sort(numbers)
    print(numbers)
