
def all_indices(arr, item, index=0):
    if index == len(arr):
        return []
    isf = all_indices(arr, item, index+1)
    if arr[index] == item:
        isf.append(index)
    return isf

if __name__ == "__main__":
    result = all_indices([1,22,33,1,4,19,7,100,24,346,57,34,789,34,213,68], 1)
    print(result)