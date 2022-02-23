def majorityElement(nums):
    count = 1
    ans = nums[0]
    for i, v in enumerate(nums):
        if i == 0:
            continue
        if count == 0:
            count = 1
            ans = v
        if v == ans:
            count += 1
        else:
            count -= 1
    return ans


if __name__ == '__main__':
    arr = [2,2,1,1,1,2,2]
    ans = majorityElement(arr)