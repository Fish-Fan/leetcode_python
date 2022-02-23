def main(nums):
    idx = 0
    lastVal = nums[0]
    for i, val in enumerate(nums):
        if i == 0:
            continue
        else:
            if val != lastVal:
                idx += 1
                nums[idx] = val
            lastVal = val
    return nums[:idx + 1]

if __name__ == '__main__':
    arr = [0,0,1,1,1,2,2,3,3,4]
    arr = main(arr)
    print(arr)

