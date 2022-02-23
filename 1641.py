def countVowelStrings(n: int) -> int:
    a, e, i, o, u = 5, 4, 3, 2, 1
    for i in range(n - 1):
        a = a + e + i + o + u
        e = e + i + o + u
        i = i + o + u
        o = o + u

    return a


if __name__ == '__main__':
    n = 2
    ans = countVowelStrings(2)
    print(ans)