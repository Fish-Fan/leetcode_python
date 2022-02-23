def partition(s: str):
    if len(s) == 0:
        return []
    ans = []
    DFS(s, [], ans, 0, 1, len(s))
    return ans


def DFS(s, path, ans, i, j, n):
    if j == n+1:
        ans.append(path[:])
    while j <= n:
        if i + 1 == j:
            DFS(s, path + [s[i:j]], ans, i + 1, j + 1, n)
        elif isPalindrome(s[i:j]):
            DFS(s, path + [s[i:j]], ans, j, j + 1, n)
        j += 1


def isPalindrome(s):
    mid = len(s) // 2
    match1 = expandAroundCentre(mid, mid, s)
    match2 = expandAroundCentre(mid, mid - 1, s)
    if match1 or match2:
        return True
    else:
        return False


def expandAroundCentre(left, right, s):
    n = len(s)
    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1
    if left == -1 and right == n:
        return True
    else:
        return False

if __name__ == '__main__':
    s = "aab"
    ans = partition(s)
    print(ans)