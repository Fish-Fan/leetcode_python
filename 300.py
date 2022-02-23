# time complexity = O(nlogn)
def lengthOfLIS(nums):
    n = len(nums)
    indices = [None for i in range(n+1)]
    length = 0
    for i, num in enumerate(nums):
        newLength = binarySearch(1, length, indices, nums, num)
        indices[newLength] = i
        length = max(length, newLength)
    return length

def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx

    middleIdx = (startIdx + endIdx) // 2
    if array[indices[middleIdx]] > num:
        endIdx = middleIdx-1
    else:
        startIdx = middleIdx+1
    return  binarySearch(startIdx, endIdx, indices, array, num)


# O(n^2) time
# def lengthOfLIS(nums) -> int:
#     n = len(nums)
#     # boundary cases
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]
#
#     dp = [1] * n
#
#     ans = dp[0]
#     for i in range(1, n):
#         maxCount = 1
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 tmp = dp[j] + 1
#                 maxCount = max(maxCount, tmp)
#         dp[i] = maxCount
#         ans = max(ans, dp[i])
#
#     return ans


if __name__ == '__main__':
    ans = lengthOfLIS([5,7,-24,12,10,2,3,12,5,6,35])
    print(ans)