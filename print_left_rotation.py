# https://www.geeksforgeeks.org/print-left-rotation-array/

def left_rotate(arr, k):
    n = len(arr)
    # k = k % n
    for i in range(n):
        print(arr[(i+k)%n],end=" ")
    print()

if __name__ == "__main__":
    list_ = [1, 3, 5, 7, 9]
    left_rotate(list_,1)
    left_rotate(list_,3)
    left_rotate(list_,4)
    left_rotate(list_,6)
