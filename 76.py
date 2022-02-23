import collections


def minWindow(s: str, t: str) -> str:
    ans = ""
    n, m = len(s), len(t)
    left, right = 0, 0
    tMap = {}
    for i in t:
        tMap[i] = i

    start, end = 0, 0
    length = float('inf')

    windowMap = {}
    while right < n:
        while right < n and len(windowMap) < m:
            if tMap.get(s[right]) != None:
                if windowMap.get(s[right]) == None:
                    windowMap[s[right]] = 1
                else:
                    windowMap[s[right]] = windowMap.get(s[right]) + 1
            right += 1

        while left < right and len(windowMap) == m:
            if right - left < length:
                length = right - left
                start, end = left, right

            if windowMap.get(s[left]) != None:
                count = windowMap.get(s[left])
                if count > 1:
                    windowMap[s[left]] = windowMap.get(s[left]) - 1
                else:
                    windowMap.pop(s[left])
            left += 1

    return s[start:end]

if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    need = collections.Counter(s)
    print(need)
