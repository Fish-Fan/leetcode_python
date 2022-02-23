def numSubarrayProductLessThanK(nums, k: int) -> int:
    left, right = 0, 0
    prod, ans = 1, 0
    while right < len(nums):
        prod *= nums[right]
        if prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        ans = right - left + 1
        right += 1
    return ans

if __name__ == '__main__':
    arr = [10,5,2,6]
    ans = numSubarrayProductLessThanK(arr, 100)
    print(ans)