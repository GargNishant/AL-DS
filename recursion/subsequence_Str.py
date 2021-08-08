

def subs(seq):
    if len(seq) == 0:
        return ['']
    first = seq[0]
    rem = seq[1:]
    list_ = subs(rem)
    result = []
    result.extend(list_)
    for item in list_:
        result.append(first+item)
    return result

if __name__ == "__main__":
    result = subs('abc')
    print(result)