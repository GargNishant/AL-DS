# https://www.youtube.com/watch?v=MOFUK3PyOPw&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=13

def display_arr(arr,idx=0):
    if idx == len(arr):
        return
    print(arr[idx])
    display_arr(arr,idx+1)


if __name__ == "__main__":
    display_arr([10,20,30,40,50],0)