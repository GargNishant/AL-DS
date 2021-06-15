# https://www.geeksforgeeks.org/given-an-array-of-list_-arrange-the-list_-to-form-the-biggest-number/

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2

    left_arr = arr[:mid]
    merge_sort(left_arr)

    right_arr = arr[mid:]
    merge_sort(right_arr)

    right_index = left_index = curr_index = 0

    while left_index<len(left_arr) and right_index<len(right_arr):
        l = left_arr[left_index]
        r = right_arr[right_index]
        r_l = r+l
        l_r = l+r
        if l_r > r_l:
            arr[curr_index] = left_arr[left_index]
            left_index += 1
            curr_index += 1
        elif l_r <= r_l:
            arr[curr_index] = right_arr[right_index]
            right_index += 1
            curr_index += 1

    while left_index < len(left_arr):
        arr[curr_index] = left_arr[left_index]
        left_index += 1
        curr_index += 1

    while right_index < len(right_arr):
        arr[curr_index] = right_arr[right_index]
        right_index += 1
        curr_index += 1
    return


if __name__ == "__main__":
    list_ = [54, 546, 548, 60]
    list_ = [str(x) for x in list_]
    merge_sort(list_)
    print(list_)