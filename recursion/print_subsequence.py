# https://youtu.be/Ke8TPhHdHMw?list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs

def print_subsequence(ques, ans=''):
    if len(ques) == 0:
        print(ans)
        return
    ch = ques[0]
    roq = ques[1:]
    print_subsequence(roq, ans + ch)
    print_subsequence(roq, ans+'')


if __name__ == "__main__":
    print_subsequence('yvtA')
