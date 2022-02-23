def majorityElement(nums):
    nums.sort()
    n = len(nums)
    i = 0
    ans = set()
    while i < n:
        count = 1
        while i + 1 < n and nums[i + 1] == nums[i]:
            count += 1
            if count > n // 3:
                ans.add(nums[i])
            i += 1
        if count == 1:
            i += 1
    return list(ans)

if __name__ == '__main__':
    nums = [1,1]
    # majorityElement(nums)
    print(list(set(nums)))