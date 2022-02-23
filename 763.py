from collections import Counter, defaultdict


def partitionLabels(s: str):
    c = Counter(s)
    d = defaultdict(int)
    ans, count = [], 0
    for i, v in enumerate(s):
        count += 1
        d[v] += 1
        if d.get(v) == c.get(v):
            flag = True
            for key in d.keys():
                if d.get(key) != c.get(key):
                    flag = False
                    break
            if flag:
                ans.append(count)
                count = 0
                d = defaultdict(int)
    return ans

if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    ans = partitionLabels(s)
    print(ans)