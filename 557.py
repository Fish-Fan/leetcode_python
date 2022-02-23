def reverse(s):
    return s[::-1]

def reversewords(s):
    arr = list(map(reverse, s.split(' ')))
    return " ".join(arr)

if __name__ == '__main__':
    s =  'Let\'s take LeetCode contest'
    ans = reversewords(s)
    print(ans)