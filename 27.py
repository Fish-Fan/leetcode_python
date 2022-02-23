def removeElement(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

if __name__ == '__main__':
    arr = [0, 1, 2, 2, 3, 0, 4, 2]
    arr = removeElement(arr, 2)
    print(arr)