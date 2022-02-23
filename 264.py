def nthUglyNumber(n):
    nthNum = 1
    num = 1
    while True:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            nthNum += 1
            if nthNum == n:
                break
        num += 1

    return num

if __name__ == '__main__':
    i2,i3,i5 = 2,3,5
    print(i2)