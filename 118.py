def generate(numRows):
    ans = []
    for i in range(numRows):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(ans[i - 1][j - 1] + ans[i - 1][j])
        ans.append(tmp)

    return ans

if __name__ == '__main__':
    num = 0
    boolean = False
    arr = []
    tuple = (0)
    if tuple:
        print('A')
    else:
        print('B')