def isValid(s: str) -> bool:
    matchMap = {}
    matchMap[']'] = '['
    matchMap['}'] = '{'
    matchMap[')'] = '('
    stack = []

    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        if len(stack) > 0 and stack[-1] == matchMap.get(c):
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    s = ']'
    ans = isValid(s)
    print(ans)