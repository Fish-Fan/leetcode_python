def insert(intervals, newInterval):
    ans = []
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda a: a[0])

    for i, arr in enumerate(intervals):
        if i == 0:
            ans.append(arr)
            continue
        preArr = ans[-1]
        if arr[1] <= preArr[1]:
            continue

        if arr[0] <= preArr[1] and arr[1] > preArr[1]:
            ans.pop()
            ans.append([preArr[0], arr[1]])
        else:
            ans.append(arr)

    return ans


if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    ans = insert(intervals, newInterval)
    print(ans)

    arr = [2,3,4]
    arr.insert(0, 1)
    print(arr)