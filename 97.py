def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    invalid = [[False for i in range(m + 1)] for j in range(n + 1)]
    return DFS(s1, s2, s3, 0, 0, 0, invalid)
def DFS(s1, s2, s3, i, j, k, invalid):
    if invalid[i][j] == True:
        return False
    if k == len(s3):
        return True
    match1, match2 = False, False
    if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
        match1 = DFS(s1, s2, s3, i + 1, j, k + 1, invalid)
    if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
        match2 = DFS(s1, s2, s3, i, j + 1, k + 1, invalid)
    valid = match1 or match2
    if not valid:
        invalid[i][j] = True
    return valid

if __name__ == '__main__':
    s1, s2, s3 = 'aa', 'ab', 'aaba'
    # print(isInterleave(s1,s2,s3))
    print(1 < float('inf'))
    print(1 > float('-inf'))
