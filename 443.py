def compress( chars) -> int:
    arr = []
    last, count = chars[0], 0
    for i, v in enumerate(chars):
        if i == 0:
            count += 1
        elif v == last:
            count += 1
        else:
            arr.append(last)
            arr.append(str(count))
            last, count = v, 1
    arr.append(last)
    arr.append(str(count))
    chars = arr
    return len(chars)

if __name__ == '__main__':
    chars = ["a","a","b","b","c","c","c"]
    ans = compress(chars)
    print(ans)