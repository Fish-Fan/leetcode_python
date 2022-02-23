def isHappy(n: int) -> bool:
    i = n
    tmpMap = {}
    while tmpMap.get(i) == None:
        tmpMap[i] = 1
        arr = []
        while i != 0:
            arr.append(i % 10)
            i = i // 10
        middleNum = 0
        for v in arr:
            middleNum += v * v
        if middleNum == 1:
            return True
        else:
            i = middleNum
    return False

if __name__ == '__main__':
    ans = isHappy(19)
    print(ans)