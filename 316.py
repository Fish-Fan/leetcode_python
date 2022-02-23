from collections import Counter
def removeDuplicateLetters( s: str) -> str:
    lMap, usedMap, arr = Counter(s), {}, []
    pos = 0
    for c in s:
        if c not in usedMap or usedMap.get(c) == False:
            popCount = 0
            for i, v in enumerate(arr[pos:]):
                if c < v and lMap.get(v) > 0:
                    popCount += 1
            for i in range(popCount):
                if lMap.get(arr[-1]) != 0:
                    l = arr.pop()
                    usedMap[l] = False
            arr.append(c)
            usedMap[c] = True
            if lMap.get(c) == 1:
                pos = len(arr) - 1
        lMap[c] -= 1
    return ''.join(arr)

if __name__ == '__main__':
    s = "bccab"
    ans = removeDuplicateLetters(s)
    print(ans)