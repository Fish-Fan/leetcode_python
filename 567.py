from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    target = Counter(s1)
    left, right = 0, len(s1)
    tmp = []
    while right <= len(s1):
        tmp.append(Counter(s2[left:right]))
        left += 1
        right += 1
    for d in tmp:
        if d == target:
            return True
    return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    ans = checkInclusion(s1, s2)
    print(ans)