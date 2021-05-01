
def print_spiral_matrix(arr,s_row=0,e_row=None,s_col=0, e_col=None):
    if e_row is None:
        e_row = len(arr)-1
    if e_col is None:
        e_col = len(arr[0])-1

    if s_row > e_row:
        return
    if s_col > e_row:
        return

    # Right Print
    print(*arr[s_row][s_col:e_col+1])
    s_row += 1

    # Down Print
    for row in range(s_row,e_row+1):
        print(arr[row][e_col])
    e_col -= 1

    # Left Print
    for col in range(e_col,s_col-1,-1):
        print(arr[e_row][col])
    e_row -= 1

    # Up Print
    for row in range(e_row,s_row-1,-1):
        print(arr[row][s_col])
    s_col += 1

    print_spiral_matrix(arr,s_row=s_row,e_row=e_row,s_col=s_col, e_col=e_col)


if __name__ == "__main__":
    matrix = [ [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
    print_spiral_matrix(matrix)