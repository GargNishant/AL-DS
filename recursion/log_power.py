# https://www.youtube.com/watch?v=O84uumjBOMY&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=9
from math import floor


def power(n:int, p_value: int):
    if p_value == 0:
        return 1
    p_n2 = power(n,floor(p_value/2))
    if p_value % 2 == 0:
        p = p_n2 * p_n2
    else:
        p = p_n2 * p_n2 * n
    return p



if __name__ == "__main__":
    result = power(2,5)
    print(result)