
def last_occ(arr, item, index=0):
    if index == len(arr):
        return -1
    lisa = last_occ(arr,item,index+1)
    if lisa == -1:
        if arr[index] == item:
            return index
        else:
            return -1
    else:
        return lisa


if __name__ == "__main__":
    result = last_occ([22,33,4,19,7,100,24,346,57,34,789,34,213,68], 100)
    print(result)