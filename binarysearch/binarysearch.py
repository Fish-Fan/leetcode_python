import bisect


def bisect_left(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def bisect_right(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == '__main__':
    nums = [7,7,7,8,8,10]
    print(bisect_left(nums, 7))
    print(bisect_right(nums, 7))
    print(bisect.bisect_left(nums, 7))
    print(bisect.bisect_right(nums, 7))
