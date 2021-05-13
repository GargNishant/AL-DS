import random


def search(arr, element):
    if len(arr) == 1:
        if arr[0] == element:
            return True
        else:
            return False
    mid = len(arr)//2

    if arr[mid] == element:
        return True
    elif arr[mid] > element:
        return search(arr[:mid],element)
    else:
        return search(arr[mid+1:],element)


if __name__ == '__main__':
    list_ = [el for el in range(10)]
    search(list_,random.randint(0,list_[-1]))