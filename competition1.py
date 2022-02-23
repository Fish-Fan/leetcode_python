from collections import Counter
def smallestSubsequence(s: str, k: int, letter: str, repetition: int) -> str:
    c = Counter(s)
    back_c = Counter()
    start = 0
    for i in range(len(s) - 1, -1, -1):
        back_c[s[i]] += 1
        c[s[i]] -= 1
        if letter in back_c and back_c[letter] == repetition:
            tmp_list = sorted(list(c.keys()))
            if tmp_list:
                first_ele = tmp_list[0]
                if first_ele > letter:
                    start = i
                    break
                else:
                    count = 0
                    j = 0
                    while count < k - repetition:
                        count += c[tmp_list[j]]
                        j += 1
                    while count != 0:
                        if s[i] in tmp_list[:j + 1]:
                            count -= 1
                        i -= 1
                    start = i
                    break
            else:
                start = i
                break
    print(start)
    # using greedy strategy until length equals k

if __name__ == '__main__':
    s = "leet"
    # k = 3
    # letter = "e"
    # repetition = 1
    # smallestSubsequence(s, k, letter, repetition)
    print(isinstance(s, str))