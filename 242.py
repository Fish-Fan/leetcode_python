from collections import Counter

if __name__ == '__main__':
    a = "anagram"
    b = "anagram"
    counter = Counter(a)
    counter1 = Counter(b)
    print(counter)
    print(a == b)