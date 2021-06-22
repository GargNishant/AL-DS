import random


def sort(arr):
    for i in range(1,len(arr)):
        # c_e = arr[i]
        if arr[i] < arr[i-1]:
            for j in range(i-1,-1,-1):
                if arr[j] < arr[j+1]:
                    break
                arr[j], arr[j+1] = arr[j+1], arr[j]

def recursive_sort(arr, index=1):
    if index == len(arr):
        return
    if arr[index] < arr[index-1]:
        recursive_swap(arr,index-1)
    recursive_sort(arr, index+1)


def recursive_swap(arr,s_i):
    if s_i == -1:
        return
    if arr[s_i] < arr[s_i+1]:
        return
    arr[s_i], arr[s_i+1] = arr[s_i+1], arr[s_i]
    recursive_swap(arr,s_i-1)


if __name__ == "__main__":
    numbers = [el for el in range(12)]
    random.shuffle(numbers)
    print(numbers)
    # sort(numbers)
    recursive_sort(numbers)
    print(numbers)