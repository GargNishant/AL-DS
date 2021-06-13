# https://www.geeksforgeeks.org/rearrange-array-arri/

def rearrange(arr):
    dict_ = {}
    for i in arr:
        dict_[i]=1
    for i in range(len(arr)):
        if dict_.get(i) is not None:
            print(i,end=" ")
        else:
            print("-1",end=" ")


if __name__ == "__main__":
    list_ = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    rearrange(list_)