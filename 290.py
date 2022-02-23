from collections import Counter

if __name__ == '__main__':
    s = "dog cat fish cat"
    arr = s.split(' ')
    print(Counter(arr))