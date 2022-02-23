def findmin(nums):
    n = len(nums) - 1
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    return nums[left]

if __name__ == '__main__':
    nums = [1,1,1,1,0]
    minNum = findmin(nums)