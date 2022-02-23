class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return "w: " + str(self.weight) + ' v:' + str(self.value)


if __name__ == '__main__':
    t, s = 4, 5
    weights, values, counts = [1,2,3,4], [2,4,4,5], [3,1,3,2]
    # coding start
    goods = []
    for i in range(t):
        k = 1
        v = values[i]
        w = weights[i]
        minus_diff = counts[i]
        while minus_diff > k:
            goods.append(Good(k * w, k * v))
            minus_diff -= k
            k = k * 2
        if minus_diff != 0:
            goods.append(Good(abs(minus_diff), abs(minus_diff) * v))
    for item in goods:
        print(item)
    # using 0,1 backpacking template
    n = len(goods)
    dp = [[0 for x in range(s + 1)] for y in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            w, v = goods[i - 1].weight, goods[i - 1].value
            if j >= w:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)