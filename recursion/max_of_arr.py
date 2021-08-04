
def max(arr, idx=0):
    if idx == len(arr)-1:
        return arr[idx]
    max_1 = max(arr,idx+1)
    if arr[idx] > max_1:
        return arr[idx]
    return max_1


if __name__ == "__main__":
    result = max([22,33,4,19,7,100,24,346,57,34,789,34,213,68])
    print(result)