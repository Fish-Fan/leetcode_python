# https://leetcode.com/problems/sort-an-array/
# LeetCode 912
# O(nlogn)Time | O(nlogn)Space
# def mergeSort(arr):
#     return mergeSortHelper(arr)
#
# def mergeSortHelper(arr):
#     if len(arr) == 1:
#         return arr
#
#     mid = len(arr) // 2
#     left_side = arr[:mid]
#     right_side = arr[mid:]
#     return doMerget(mergeSortHelper(left_side), mergeSortHelper(right_side))
#
# def doMerget(left_arr, right_arr):
#     arr = [None] * (len(left_arr) + len(right_arr))
#     i, j, k = 0, 0, 0
#     while i < len(left_arr) and j < len(right_arr):
#         if left_arr[i] <= right_arr[j]:
#             arr[k] = left_arr[i]
#             i += 1
#         else:
#             arr[k] = right_arr[j]
#             j += 1
#         k += 1
#
#     while i < len(left_arr):
#         arr[k] = left_arr[i]
#         i += 1
#         k += 1
#
#     while j < len(right_arr):
#         arr[k] = right_arr[j]
#         j += 1
#         k += 1
#     return arr

# O(nlogn)Time | O(n)Space
def mergeSort(arr):
    mergeSortHelper(arr, 0, len(arr)-1, arr[:])
    return arr
def mergeSortHelper(arr, left, right, auxiliary_arr):
    if left == right:
        return

    mid = (left + right) // 2
    # check this point, swap the position of arr and auxiliary
    mergeSortHelper(auxiliary_arr, left, mid, arr)
    mergeSortHelper(auxiliary_arr, mid+1, right, arr)
    return doMerge(arr, auxiliary_arr, left, right, mid)

def doMerge(arr, auxiliary_arr, left, right, mid):
    i, j, k = left, mid+1, left
    while i <= mid and j <= right:
        if auxiliary_arr[i] <= auxiliary_arr[j]:
            arr[k] = auxiliary_arr[i]
            i += 1
        else:
            arr[k] = auxiliary_arr[j]
            j += 1
        k += 1

    while i <= mid:
        arr[k] = auxiliary_arr[i]
        i += 1
        k += 1

    while j <= right:
        arr[k] = auxiliary_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    ans = mergeSort(nums)
    print(ans)