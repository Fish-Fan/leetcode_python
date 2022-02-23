import heapq
def evalRPN(tokens) -> int:
    stack = []
    for token in tokens:
        if token == '+' or token == '-' or token == '*' or token == '/':
            num2, num1 = int(stack.pop()), int(stack.pop())
            if token == '+':
                stack.append(num1 + num2)
            if token == '-':
                stack.append(num1 - num2)
            if token == '*':
                stack.append(num1 * num2)
            if token == '/':
                positive = (num1 < 0) is (num2 < 0)
                tmp = abs(num1) // abs(num2)
                if positive:
                    stack.append(-tmp)
                else:
                    stack.append(tmp)
        else:
            stack.append(token)
    return stack.pop()

if __name__ == '__main__':
    tokens = ["4","13","5","/","+"]
    ans = evalRPN(tokens)
    print(ans)

    h = []
    heapq.heappush(h, (2,'2'))
    heapq.heappush(h, (1, '1'))
    heapq.heappush(h, (3, '3'))
    print(heapq.heappop(h))