# https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/

def find_max(arr):
    results = []
    arr = arr
    for i in range(len(arr)):
        first = arr[0]
        arr = arr[1:]
        arr.append(first)
        results.append(get_sum(arr))
    return max(results)


def get_sum(arr_):
    sum = 0
    for i in range(len(arr_)):
        sum += i*arr_[i]
    return sum


if __name__ == "__main__":
    list_ = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(find_max(list_))