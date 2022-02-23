def rotate(nums, k):
    n = len(nums)
    k = k % n
    arr1 = []
    for i in range(n-k):
        arr1.append(nums[i])


    for i, v in enumerate(nums):
        if i < k:
            nums[i] = nums[n - k + i]
        else:
            break

    for i in range(k,n,1):
        nums[i] = arr1.pop(0)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 10
    rotate(nums, k)
    a = float('inf')
    print(a == float('inf'))
    Aset = set()
    Aset.add(1)
    Aset.add(2)
    Aset.add(2)
    print(Aset)
    s = "ABC"
    tMap = {}
    tMap['A'] = 1
    tMap['B'] = 2
    tMap.pop('A')
    print(tMap)