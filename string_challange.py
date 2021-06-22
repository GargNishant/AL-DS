
def string_challenge(arr):
    result = ''
    for i in range(len(arr)-1):
        result += arr[i]
        if arr[i] == '0' or arr[i+1] == '0':
            continue
        elif int(arr[i])%2 == 0 and int(arr[i+1])%2 == 0:
            result += '*'
        elif not int(arr[i])%2 == 0 and not int(arr[i+1])%2 == 0:
            result += '-'
    result += arr[-1]
    return result


if __name__ == "__main__":
    print(string_challenge('12344456667777077700'))