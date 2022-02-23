def thirdMax( nums) -> int:
    n = len(nums)
    ansIdx = n - 3
    left, right = 0, n - 1
    while left <= right:
        pivot = partition(left, right, nums)
        if pivot < ansIdx:
            left += 1
        elif pivot > ansIdx:
            right -= 1
        else:
            break
    return nums[ansIdx]


def partition( left, right, nums):
    pivot = right
    pivotValue = nums[right]
    right -= 1
    while left <= right:
        if nums[left] < pivotValue:
            left += 1
        elif nums[right] > pivotValue:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    nums[left], nums[pivot] = nums[pivot], nums[left]
    return left

if __name__ == '__main__':
    arr = [3,5,2,1,9,2,4,5]
    arr = list(set(arr))
    ans = thirdMax(arr)
    print(ans)

    arr = [i for i in range(10)]
    print(arr)