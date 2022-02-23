def fractionToDecimal(numerator, denominator):
    num, deno = abs(numerator), abs(denominator)
    ans = str(num // deno)
    if (numerator > 0) ^ (denominator > 0):
        ans = '-' + ans
    if num % deno == 0:
        return ans
    else:
        ans += '.'

    tmpMap = {}
    
    while num % deno != 0:
        num = num * 10
        result = num // deno
        if tmpMap.get(num) != None:
            ans = ans[:tmpMap.get(num)] + '(' + ans[tmpMap.get(num):] + ')'
            break
        else:
            ans += str(result)
            tmpMap[num] = len(ans) - 1
        num = num % deno
    return ans

if __name__ == '__main__':
    fractionToDecimal(22, 7)
