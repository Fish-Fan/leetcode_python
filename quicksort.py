def quicksort(nums):
    return quicksortHelper(nums, 0, len(nums)-1)
def quicksortHelper(nums, left, right):
    if left <= right:
        pivotIdx = partition(nums, left, right)
        quicksortHelper(nums, left, pivotIdx-1)
        quicksortHelper(nums, pivotIdx+1, right)
    return nums

def partition(nums, left, right):
    pivot = nums[right]
    pivotIdx = right
    right -= 1
    while left <= right:
        if nums[left] < pivot:
            left += 1
        elif nums[right] > pivot:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    nums[left], nums[pivotIdx] = nums[pivotIdx], nums[left]
    return left


if __name__ == '__main__':
    # nums = [3,2,3,1,2,4,5,5,6]
    # sorted_nums = quicksort(nums)
    # print(sorted_nums)

    s = "abc"
    s += "a"
    print(s)