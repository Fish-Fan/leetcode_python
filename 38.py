def countAndSay(n: int):
    dp = [""] * n
    for i in range(n):
        number = ""
        if i == 0:
            number = "1"
        elif i == 1:
            number = "11"
        else:
            preStr = dp[i - 1]
            start = 0
            length = len(preStr)
            left, right = 0, 0
            while right < length:
                count, character = 0, preStr[left]
                while right < length and preStr[left] == preStr[right]:
                    right += 1
                count = right - left
                number += str(count)
                number += character
                left = right

        dp[i] = number
    return dp[-1]

if __name__ == '__main__':
    n = 5
    ans = countAndSay(n)
    s = "abc"
    arr = [1,2,3]
    arr.reverse()
    print(arr)
    for i,v in enumerate(s):
        print('index: ' + str(i) + ' v: ' + v)