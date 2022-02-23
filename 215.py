# O(n)Time | O(1)Space
def findKthLargest(nums, k: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        pivotIdx = partition(nums, left, right)
        if pivotIdx - left + 1 > k:
            right = pivotIdx - 1
        elif pivotIdx - left + 1 < k:
            k = k - (pivotIdx - left + 1)
            left = pivotIdx + 1
        else:
            return nums[pivotIdx]
    return 0


def partition(nums, left, right):
    pivot = nums[right]
    pivotIdx = right
    right -= 1
    while left <= right:
        if nums[left] >= pivot:
            left += 1
        elif nums[right] <= pivot:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    nums[left], nums[pivotIdx] = nums[pivotIdx], nums[left]
    return left

if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    ans = findKthLargest(nums, 4)
    print(ans)