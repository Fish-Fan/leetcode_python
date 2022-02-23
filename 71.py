def simplifyPath(path: str) -> str:
    arr = path.split('/')
    pathDict = []
    for v in arr:
        if v == '.' or not v:
            continue
        elif v == '..' and len(pathDict) > 0:
            pathDict.pop()
        elif v != '..':
            pathDict.append(v)

    ans = '/'
    for v in pathDict:
        ans += v + '/'
    if len(ans) == 1:
        return ans
    else:
        return ans[:len(ans)-1]


if __name__ == '__main__':
    s = '/../'
    ans = simplifyPath(s)
    print(ans)



