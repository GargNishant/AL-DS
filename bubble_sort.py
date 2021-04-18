import random


def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


if __name__ == "__main__":
    numbers = [el for el in range(10000)]
    random.shuffle(numbers)
    print(numbers)
    sort(numbers)