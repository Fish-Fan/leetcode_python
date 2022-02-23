class Solution:
    nums = []
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, i:int, j:int) -> int:
        ans = 0
        for i in range(i,j+1):
            ans += self.nums[i]
        return ans

if __name__ == '__main__':
    obj = Solution([1,2,3,4,5,6])
    ans = obj.sumRange(1,2)
    print(ans)
    print('start')
    for i in range(5,0,-1):
        print(i)