# O(n^2)Time | O(1)Space
def InsertSort(arr):
    for i in range(1, len(arr)):
        while i >= 1 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return arr

if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    ans = InsertSort(nums)
    print(ans)
