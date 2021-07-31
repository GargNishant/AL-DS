# https://www.youtube.com/watch?v=_O6geLdoSV4&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=15

def display_arr(arr,idx=0):
    if idx == len(arr):
        return
    display_arr(arr,idx+1)
    print(arr[idx])


if __name__ == "__main__":
    display_arr([10,20,30,40,50])