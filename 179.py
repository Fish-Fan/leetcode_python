def largestNumber(nums) -> str:
    nums = quicksort(nums)
    numsStr = []
    for i in nums:
        numsStr.append(str(i))
    return ''.join(numsStr)


def quicksort(nums):
    return quicksortHelper(nums, 0, len(nums)-1)


def quicksortHelper(nums, left, right):
    if left <= right:
        pivotIdx = partition(nums, left, right)
        quicksortHelper(nums, pivotIdx + 1, right)
        quicksortHelper(nums, left, pivotIdx - 1)
    return nums


def partition(nums, left, right):
    pivot = nums[right]
    pivotIdx = right
    right -= 1

    while left <= right:
        if compare(nums[left], pivot):
            left += 1
        elif compare(pivot, nums[right]):
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    nums[left], nums[pivotIdx] = nums[pivotIdx], nums[left]
    return left


def compare( num1, num2):
    if str(num1) + str(num2) > str(num2) + str(num1):
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [999999991,9]
    ans = largestNumber(nums)
    print(ans)
    a = '00'
    print(a.lstrip('0'))