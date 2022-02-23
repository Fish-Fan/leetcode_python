def diffWaysToCompute( expression: str):
    ans = []
    if expression and ('+' not in expression and '-' not in expression and '*' not in expression):
        ans.append(int(expression))
        return ans

    for i, v in enumerate(expression):
        if v == '+' or v == '-' or v == '*':
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i + 1:])
            for m in left:
                for n in right:
                    res = calculate(m, n, v)
                    ans.append(res)
    return ans


def calculate( num1, num2, operator):
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    else:
        return num1 * num2
    
if __name__ == '__main__':
    s = "-10"
    ans = diffWaysToCompute(s)
    print(ans)