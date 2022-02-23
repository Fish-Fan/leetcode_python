from collections import Counter
def findLongestWord(s: str, dictionary) -> str:
    c = Counter(s)
    ans, length = [], 0
    for word in dictionary:
        d, i, length = c.copy(), 0, length
        for letter in s:
            if i == len(word):
                break
            elif letter == word[i]:
                i += 1
            d[letter] -= 1
        if i == len(word):
            length = max(length, len(word))
            ans.append(word)

    if len(ans) > 0:
        tmp = []
        for word in ans:
            if len(word) == length:
                tmp.append(word)
        tmp.sort()
        return tmp[0]
    else:
        return ""


if __name__ == '__main__':
    dictionary = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
    s = "abpcplea"
    ans = findLongestWord(s, dictionary)
    print(ans)