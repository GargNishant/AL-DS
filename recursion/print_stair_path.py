
def print_stair_path(n, path_so_far=''):
    if n == 0:
        print(path_so_far)
        return
    if n < 0:
        return
    print_stair_path(n-1,path_so_far+"1")
    print_stair_path(n-2,path_so_far+"2")
    print_stair_path(n-3,path_so_far+"3")


if __name__ == "__main__":
    print_stair_path(4)