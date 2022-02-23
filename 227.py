def calculate(s):
    num, stack, sign = 0, [], '+'
    for i, v in enumerate(s):
        if v >= '0' and v <= '9':
            num = num * 10 + int(v)
        if v in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                stack.append(stack.pop() * num)
            if sign == '/':
                tmp = stack.pop()
                if tmp > 0:
                    stack.append(tmp // num)
                else:
                    stack.append(-(tmp // -num))
            num = 0
            sign = v
    return sum(stack)

if __name__ == '__main__':
    s = '14-3/2'
    ans = calculate(s)
    print(ans)