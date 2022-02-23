from collections import defaultdict
def checkValidString( s: str) -> bool:
    left_stack = []
    star_stack = []
    for i, v in enumerate(s):
        if v == '(':
            left_stack.append(i)
        elif v == '*':
            star_stack.append(i)
        else:
            if left_stack:
                left_stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    if len(left_stack) == 0:
        return True
    if len(left_stack) != 0 and len(star_stack) == 0:
        return False
    print(left_stack)
    print(star_stack)
    while left_stack[-1] < star_stack[-1]:
        left_stack.pop()
        star_stack.pop()
    if len(left_stack) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "((**"
    ans = checkValidString(s)
    print(ans)