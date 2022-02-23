def removeKdigits(num: str, k: int) -> str:
    n = len(num)
    if n == k:
        return '0'
    while len(num) > n - k:
        tmpArr = []
        maxPos, maxNum = 0, int(num[0:n - k])
        for i in range(len(num) - k):
            curNum = int(num[i:n - k + i])
            tmpArr.append(curNum)
            if curNum > maxNum:
                maxNum = curNum
                maxPos = i
        num1 = num[:maxPos] + num[maxPos + 1:]
        num2 = num[:-1]
        if num2 < num1:
            num = num2
        else:
            num = num1
    return str(int(num))

if __name__ == '__main__':
    num = '43214321'
    ans = removeKdigits(num, 4)
    print(ans)