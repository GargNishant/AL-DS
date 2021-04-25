import random
import time


def sort(arr):
    if len(arr) <= 1:
        # Returns when a single element in remaining, as it cannot be further divided
        return
    mid = len(arr)//2

    # Store the left side at this recursion level, for merging during returns. At lowest level it will have 1 element
    left_side = arr[:mid]
    sort(left_side)
    # Store the Right side at this recursion level, for merging during returns. At lowest level it will have 1 element
    right_side = arr[mid:]
    sort(right_side)

    left_index = right_index = curr_index = 0
    """
    5	1
    9	6
    10	8
    12	23
    17	27
    20	30
    25	35
    
    While loop over both
    l=0, r=0, c=0
    5 < 1:
    1
    l=0, r=1,c=1
    5<6:
    1,5
    l=1, r=1,c=2
    9<6:
    1,5,6
    l=1, r=2,c=3
    9<8:
    1,5,6,8
    l=1, r=3,c=4
    9<23:
    1,5,6,8,9
    l=2, r=3,c=5
    10<23:
    1,5,6,8,9,10
    l=3, r=3, c=6
    12<23:
    1,5,6,8,9,10,12
    l=4, r=3, c=7
    17<23:
    1,5,6,8,9,10,12,17
    l=5, r=3, c=8
    20<23:
    1,5,6,8,9,10,12,17,20
    l=6, r=3, c=9
    25<23:
    1,5,6,8,9,10,12,17,20,23
    l=6, r=4, c=10
    25<27:
    1,5,6,8,9,10,12,17,20,23,25
    l=7,r=4,c=11
    
    l=7=len(left_arr)
    
    fill the Remaining, in this case from Right
    1,5,6,8,9,10,12,17,20,23,25 ->
    1,5,6,8,9,10,12,17,20,23,25,27,30,35
    """

    # We will store the sorted values in arr, as arr, is of no use, and all the data
    # copied into left and right arr.
    # This loop will run until at least one of the array is empty
    while left_index < len(left_side) and right_index < len(right_side):
        if left_side[left_index] < right_side[right_index]:
            arr[curr_index] = left_side[left_index]
            left_index += 1
        else:
            arr[curr_index] = right_side[right_index]
            right_index += 1
        curr_index += 1

    # There can be cases of leftovers. The leftovers will be only from 1 Array and not 2 array
    # The following 2 loops handles them
    while left_index < len(left_side):
        arr[curr_index] = left_side[left_index]
        curr_index += 1
        left_index += 1

    while right_index < len(right_side):
        arr[curr_index] = right_side[right_index]
        curr_index += 1
        right_index += 1
    return


if __name__ == "__main__" :
    numbers = [el for el in range(60000)]
    random.shuffle(numbers)
    # print(numbers)
    t0 = time.time()
    sort(numbers)
    t1 = time.time() - t0
    print("Time elapsed: ", t1)
    # print(numbers)
