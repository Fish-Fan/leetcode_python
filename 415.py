def addStrings(num1: str, num2: str) -> str:
    stack1, stack2 = [], []
    for v in num1:
        stack1.append(v)
    for v in num2:
        stack2.append(v)
    carry, arr = 0, []
    while stack1 and stack2:
        n1, n2 = int(stack1.pop()), int(stack2.pop())
        tmp = n1 + n2 + carry
        arr.append(str(tmp // 10))
        carry = tmp % 10
    while stack1:
        n1 = int(stack1.pop())
        tmp = n1 + carry
        arr.append(str(tmp // 10))
        carry = tmp % 10
    while stack2:
        n2 = int(stack2.pop())
        tmp = n2 + carry
        arr.append(str(tmp // 10))
        carry = tmp % 10
    if carry != 0:
        arr.append(str(carry))
    arr.reverse()
    return "".join(arr)


if __name__ == '__main__':
    num1 = '11'
    num2 = '123'
    ans = addStrings(num1, num2)
    print(ans)