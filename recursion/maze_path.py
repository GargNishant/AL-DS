
def get_path(s_row=1, s_col=1, d_row=5, d_col=5):
    if s_row == d_row and s_col == d_col:
        return ['']

    h_paths = []
    v_paths = []
    if s_row < d_row:
        v_paths = get_path(s_row+1,s_col,d_row,d_col)
    if s_col < d_col:
        h_paths = get_path(s_row,s_col+1,d_row,d_col)
    paths = []

    for path in h_paths:
        paths.append('h'+path)
    for path in v_paths:
        paths.append('v'+path)
    return paths

if __name__ == "__main__":
    result = get_path(d_row=3,d_col=3)
    print(result)