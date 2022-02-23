
def findUnsortedSubarray(nums) -> int:
    if len(nums) == 1:
        return 0
    start, end = 0, len(nums) - 1
    while start < len(nums):
        if start > 0 and nums[start] <= nums[start - 1]:
            break
        start += 1
    if start == len(nums):
        return 0
    while end > 0:
        if end < len(nums) - 1 and nums[end - 1] >= nums[end]:
            break
        end -= 1

    return end - start + 3


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    ans = findUnsortedSubarray(nums)
    print(ans)