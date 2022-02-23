def lengthOfLastWord(s: str) -> int:
    count = 0
    for v in enumerate(s):
        if not v.isspace():
            count += 1
        else:
            count = 0
    return count


if __name__ == '__main__':
    s = 'hello world'
    ans = lengthOfLastWord(s)