def nextPermutation(nums):
    # find the pivot
    idx, l = len(nums) - 1, len(nums) - 1
    while idx - 1 >= 0 and nums[idx - 1] > nums[idx]:
        idx -= 1

    # the last permutation
    if idx == 0:
        nums.reverse()
    pivotIdx = idx - 1
    pivot = nums[pivotIdx]

    # swap the pivot and the minimum num in the suffix which greater than pivot
    left, right = idx, l
    target = nums[left]
    targetIdx = left
    while left <= right:
        if nums[left] > pivot and nums[left] < target:
            targetIdx = left
            target = nums[left]
        left += 1

    temp = nums[pivotIdx]
    nums[pivotIdx] = nums[targetIdx]
    nums[targetIdx] = temp

    # aescdending the suffix == reverse(coz is ordered)
    suffix = nums[idx:]
    suffix.reverse()
    nums = nums[:idx] + suffix
    return nums

if __name__ == '__main__':
    arr = [1,4,3,2]
    ans = nextPermutation(arr)
    print(ans)