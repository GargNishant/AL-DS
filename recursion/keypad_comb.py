
def get_combination(keys, map):
    if len(keys) == 0:
        return ['']
    cfsk = get_combination(keys[1:],map)
    result = []
    ck = keys[0]
    pmap = map[ck]
    for key in pmap:
        for comb in cfsk:
            result.append(key+comb)
    return result

if __name__ == "__main__":
    map_ = {'1':'ab', '2':'cd','3':'de'}
    print(get_combination('123',map_))