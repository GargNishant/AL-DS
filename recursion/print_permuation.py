# https://youtu.be/K5xJXbnYMBc?list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs

def print_permutation(sequence, asf=''):
    if len(sequence) == 0:
        print(asf)
        return
    for i in range(len(sequence)):
        ch = sequence[i]
        lpq = sequence[:i]
        rpq = sequence[i+1:]
        roq = lpq + rpq
        print_permutation(roq,asf+ch)


if __name__ == "__main__":
    print_permutation('abcd')