
def print_maze(s_row=1, s_col=1, d_row=5, d_col=5, path_so_far=''):
    if s_row == d_row and s_col == d_col:
        print(path_so_far)
        return
    if s_row < d_row:
        print_maze(s_row+1,s_col,d_row, d_col,path_so_far+'v')
    if s_col < d_col:
        print_maze(s_row,s_col+1, d_row,d_col,path_so_far+'h')


if __name__ == "__main__":
    print_maze(d_row=10, d_col=10)