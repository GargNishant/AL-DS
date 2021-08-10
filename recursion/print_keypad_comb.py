# https://youtu.be/4yMtvToiJE0?list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs

def print_keypad_combination(ques,codes, ans=''):
    if len(ques) == 0:
        print(ans)
        return
    ch = ques[0]
    roq = ques[1:]
    code_for_ch = codes[ch]
    for i in range(len(code_for_ch)):
        cho = code_for_ch[i]
        print_keypad_combination(roq,codes,ans+cho)


if __name__ == "__main__":
    map_ = {'1': 'ab', '2': 'cd', '3': 'de'}
    print_keypad_combination('123',map_)