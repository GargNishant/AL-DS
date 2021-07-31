# https://www.youtube.com/watch?v=KYke5cn9jAk&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=7

def power(n:int, p_value: int):
    if p_value == 1:
        return n
    p_1 = power(n,p_value-1)
    p = n * p_1
    return p

if __name__ == "__main__":
    result = power(3,6)
    print(result)