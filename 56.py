def merge(intervals):
    # sort
    temp = sorted(intervals, key=lambda a: a[0])

    ans = []
    for i, arr in enumerate(temp):

        if i == 0:
            ans.append(arr)
            continue

        preArr = ans[-1]
        if arr[0] <= preArr[1] and arr[1] >= preArr[1]:
            preArr[1] = arr[1]

        if arr[0] > preArr[1]:
            ans.append(arr)

    return ans

if __name__ == '__main__':
    merge([[1,3],[2,6],[8,10],[15,18]])