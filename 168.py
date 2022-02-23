def convertToTitle(columnNumber: int) -> str:
    lMap, letterArr = {}, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i, v in enumerate(letterArr):
        lMap[i + 1] = v
    lMap[0] = 'Z'
    arr = []
    carry = columnNumber % 26
    while carry > 0:
        c = lMap.get(carry)
        arr.append(c)
        columnNumber = columnNumber // 26
        carry = columnNumber % 26
    reverseArr = []
    while arr:
        reverseArr.append(arr.pop())
    return ''.join(reverseArr)

if __name__ == '__main__':
    num1, num2 = '34', '30'
    print(num1 > num2)
