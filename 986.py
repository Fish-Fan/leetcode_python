def intervalIntersection(firstList, secondList):
    length = max(firstList[-1][-1], secondList[-1][-1]) + 1
    arr = [0] * length

    for item in firstList:
        start, end = item[0], item[1]
        for i in range(start, end):
            arr[i] = 1

    for item in secondList:
        start, end = item[0], item[1]
        for i in range(start, end):
            if arr[i] == 1:
                arr[i] = 2

    start, end = 0, 0
    ans = []
    i = 0
    while i < len(arr):
        if (i > 0 and arr[i - 1] != 2 and arr[i] == 2) or (i == 0 and arr[i] == 2):
            start = i
            while i < len(arr) and arr[i] == 2:
                i += 1
            end = i - 1
            ans.append([start, end])
        i += 1
    return ans

if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    ans = intervalIntersection(firstList, secondList)