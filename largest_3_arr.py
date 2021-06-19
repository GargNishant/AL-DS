# https://www.geeksforgeeks.org/find-the-largest-three-elements-in-an-array/

def find(arr):
    l_1 = arr[0]
    l_2 = None
    l_3 = None
    for index in range(1,len(arr)):
        if arr[index] > l_1:
            l_3, l_2, l_1 = l_2, l_1, arr[index]
        if arr[index] < l_1:
            if l_2 is None:
                l_2 = arr[index]
            elif arr[index] > l_2:
                l_3, l_2 = l_2, arr[index]
            elif l_3 is None or arr[index] > l_3:
                l_3 = arr[index]

    print(l_1, l_2, l_3)


if __name__ == "__main__":
    list_ = [12, 13, 1, 10, 34, 1]
    find(list_)
