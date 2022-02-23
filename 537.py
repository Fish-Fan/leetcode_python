def complexNumberMultiply(num1: str, num2: str) -> str:
    nums1, nums2 = num1.split('+'), num2.split('+')
    real1, img1 = int(nums1[0]), int(nums1[1][:-1])
    real2, img2 = int(nums2[0]), int(nums2[1][:-1])
    real = real1 * real2 - img1 * img2
    img = real1 * img2 + real2 * img1
    ans = str(real) + "+" + str(img) + "i"
    return ans

if __name__ == '__main__':
    num1, num2 = '1+-1i', '1+-1i'
    ans = complexNumberMultiply(num1, num2)
    print(ans)