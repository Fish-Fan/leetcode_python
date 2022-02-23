def findPeakElement(nums):
    n = len(nums)
    left, right = 0, n - 1
    if n == 1:
        return 0
    if n >= 2 and nums[0] > nums[1]:
        return 0

    '''
    If num[i-1] < num[i] > num[i+1], then num[i] is peak
    If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
    If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
    If num[i-1] > num[i] < num[i+1], then both sides have peak
    '''
    while left < right:
        mid = (left + right) // 2
        while left < right:
            if mid - 1 >= 0 and mid + 1 < n and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif mid - 1 >= 0 and mid + 1 < n and nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif mid - 1 >= 0 and mid + 1 < n and nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1

    return left

if __name__ == '__main__':
    arr = [1,2,3,1]
    findPeakElement(arr)