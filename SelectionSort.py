# O(n^2)Time | O(1)Space
def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx, min_val = i, arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_val:
                min_idx = j
                min_val = arr[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    ans = SelectionSort(nums)
    print(ans)