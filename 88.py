def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    ans = []
    i, start = 0, 0
    while i < m + n:
        if start == n and i == m:
            break
        if start == n or (i < m and nums1[i] <= nums2[start]):
            ans.append(nums1[i])
            i += 1
        elif start < n:
            ans.append(nums2[start])
            start += 1
        else:
            break

    nums1 = ans
    return nums1
if __name__ == '__main__':
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
