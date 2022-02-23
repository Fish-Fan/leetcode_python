# ---------------search target------------------
# only use when there is an order list, no matter contains duplicates or not
# O(log(n)) Time, O(1) Space
def binarySearch(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr)-1)

def binarySearchHelper(arr, target, left, right):
    while (left <= right):
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1


# return the target pos or first greater pos, no matter contains duplicates or not
# leetcode->34
def firstGreaterOrEqual(nums, target):
    left, right = 0, len(nums)
    while left < right: # must be <, or there is a dead loop, consider this case[1,1,1,1,1], target=1
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# -----------------------find the minimum number(only for rotated arr)------------------
# Only suitable for arr that does not contain duplicates
# leetcode->33
def findminWithoutDuplicates(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# no matter contains duplicates or not
# leetcode->154
def findmin(nums):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[left] < nums[right]:
            left = mid + 1
        elif nums[left] > nums[right]:
            right = mid
        else:
            right -= 1
    return nums[left]

# only for rotate array like [4,5,6,7,1,2,3] [4,5,6,7,0,1,2]
def binarysearchforSmallestNumber(nums):
    return binarysearchforSmallestNumberHelper(nums, 0, len(nums)-1)
def binarysearchforSmallestNumberHelper(nums, left, right):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def myBinarySearch(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    arr = [1,2,3,5,6]
    print(sum(arr))
    pos = firstGreaterOrEqual(arr, 7)
    print("firstGreaterOrEqual: " + str(pos))

    pos = myBinarySearch(arr, 0, len(arr)-1, 6)
    print("binarysearch: " + str(pos))

