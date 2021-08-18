# https://www.youtube.com/watch?v=jUo0Qis4FKU&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=44

def print_encodings(ques, ans=''):
    if len(ques) == 0:
        print(ans)
        return
    ch = ques[0]
    code = mapping.get(ch)
    if code is None:
        return
    roq = ques[1:]
    print_encodings(roq,ans+code)
    if len(ques) >= 2:
        ch = ques[:2]
        code = mapping.get(ch)
        if code is None:
            return
        roq = ques[2:]
        print_encodings(roq, ans + code)


if __name__ == "__main__":
    mapping = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l',
               '13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w',
               '24':'x','25':'y','26':'z'}
    print_encodings('279')