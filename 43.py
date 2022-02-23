def multiply(num1, num2):
    m, n = len(num1), len(num2)
    arr = [0] * (m + n)

    for j in range(n):
        for i in range(m):
            a, b = int(num1[m - i-1]), int(num2[n - j-1])
            pos1, pos2 = i + j, i + j + 1
            mul = a * b + arr[pos1]

            arr[pos1] = mul % 10
            arr[pos2] += mul // 10
    # remove the redundant zero
    start = False
    s = []
    arr.reverse()
    for i, v in enumerate(arr):
        if v != 0 and not start:
            start = True
        if start:
            s.append(str(v))
    if not start:
        return "0"
    return "".join(s)

def multiply1(num1: str, num2: str) -> str:
    arr = []
    l1, l2 = len(num1), len(num2)
    for j in range(l2):
        for i in range(l1):
            n1, n2 = int(num1[l1-i-1]), int(num2[l2-j-1])
            tmp = [0] * (i + j + 2)
            result = n1 * n2
            count = 1
            while result != 0:
                p = result % 10
                if count == 1:
                    tmp[i + j] = p
                else:
                    tmp[i + j + 1] = p
                result = result // 10
                count += 1
            arr.append(tmp)


    tmp = []
    carry = 0
    for i in range(l1 + l2 + 2):
        num = 0
        for item in arr:
            n = len(item)
            if i < n:
                num += item[i]
        tmp.append(str((num + carry) % 10))
        carry = (num + carry) // 10
    while carry != 0:
        tmp.append(str(carry%10))
        carry = carry%10
    tmp.reverse()
    count = 0
    for i,v in enumerate(tmp):
        if v != '0':
            count = i
            break
    if count == 0:
        return "0"
    else:
        tmp = tmp[count:]
    s = "".join(tmp)
    return s

if __name__ == '__main__':
    num1, num2 = '0', '0'
    ans = multiply(num1, num2)
    print(ans)

    s = "abc  cba"
    tmp = s.split(' ')
    print(tmp[-1])
