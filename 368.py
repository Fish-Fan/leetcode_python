class Solution:
    class Pair:
        def __init__(self, num, pre, l):
            self.num = num
            self.pre = pre
            self.l = l

    def largestDivisibleSubset(self, nums):
        n = len(nums)
        if n == 0:
            return []

        nums.sort()
        pairArr = []
        for i in nums:
            pairArr.append(Solution.Pair(i, -1, -1))

        maxPair = pairArr[0]
        for i in range(1, n):
            pair = pairArr[i]
            for j in range(i):
                prePair = pairArr[j]
                if pair.num % prePair.num == 0 and pair.l <= prePair.l + 1:
                    pair.pre = j
                    pair.l = prePair.l + 1

            if pair.l > maxPair.l:
                maxPair = pair

        ansArr = []
        while True:
            pre = maxPair.pre
            ansArr.append(maxPair.num)
            if pre == -1:
                break

            maxPair = pairArr[maxPair.pre]

        return ansArr

if __name__ == '__main__':
    arr = [4,8,10,240]
    s = Solution()
    ans = s.largestDivisibleSubset(nums=arr)
    print(ans)

    print('test')
    for i in range(2):
        print(i)