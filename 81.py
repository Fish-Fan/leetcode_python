def search(nums, target):
    # using binarysearch to find the smallest number
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    idx = 0
    if target > nums[0]:
        idx = binarysearch(nums, target, 0, left-1)
    elif target < nums[0]:
        idx = binarysearch(nums, target, left, n-1)
    else:
        return True

    if nums[idx] == target:
        return True
    else:
        return False


def binarysearch(nums, target, left, right):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

if __name__ == "__main__":
    arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    ans = search(arr, 2)