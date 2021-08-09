
def get_stairs_path(n):
    if n == 0:
        return ['']
    elif n < 0:
        return []
    nm1 = get_stairs_path(n-1)
    nm2 = get_stairs_path(n-2)
    nm3 = get_stairs_path(n-3)
    paths = []
    for path in nm1:
        paths.append('1'+path)
    for path in nm2:
        paths.append('2'+path)
    for path in nm3:
        paths.append('3'+path)
    return paths


if __name__ == "__main__":
    result = get_stairs_path(5)
    print(result)