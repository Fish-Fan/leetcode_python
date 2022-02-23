def restoreIpAddresses(s: str):
    arr = []
    DFS(s, 0, [], arr)
    ans = []
    for v in arr:
        ans.append('.'.join(v))
    return ans


def DFS(s, level, path, ans):
    if not s:
        if level == 4:
            ans.append(path[:])
        return

    for i in range(1, 4):
        tmp = s[:i]
        if tmp[0] != '0' or (len(tmp) == 1 and tmp[0] == '0'):
            tmpNumber = int(tmp)
            if i <= len(s) and tmpNumber >= 0 and tmpNumber <= 255:
                path.append(tmp)
                DFS(s[i:], level + 1, path, ans)
                path.pop()
            else:
                continue

if __name__ == '__main__':
    s = '101023'
    ans = restoreIpAddresses(s)
    print(ans)