from collections import Counter


def findPairs(nums, k: int) -> int:
    # corner cases:
    if k < 0:
        return 0
    c = Counter(nums)
    setNums = list(c.keys())
    d = {}
    ans = 0
    if k > 0:
        for i in setNums:
            num1, num2 = i + k, i - k
            if i in d:
                continue
            if num1 in c or num2 in c:
                d[num1] = 1
                d[num2] = 1
                ans += 1


    elif k == 0:
        for i in setNums:
            if c.get(i) > 1:
                ans += 1
    return ans


if __name__ == '__main__':
    arr = [1,1,3,4,5]
    ans = findPairs(arr, 2)
    print(ans)