from _collections import defaultdict

if __name__ == '__main__':
    # defaultdict argument is list
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(d)

    # defaultdict argument is int
    s = 'fanyank'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print(d)

