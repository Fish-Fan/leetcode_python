def plusOne(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        digit = digits[i] + carry
        carry = digit // 10
        digits[i] = digit % 10

    if carry != 0:
        digits.insert(0, carry)
    return digits

if __name__ == '__main__':
    digits = [9,9]
    ans = plusOne(digits)
    print(ans)