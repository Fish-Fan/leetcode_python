def canPlaceFlowers(flowerbed, n) -> bool:
    flowerbed.insert(len(flowerbed), 0)
    flowerbed.insert(0, 0)
    count_0, count_1 = 0, 0
    for i in flowerbed:
        if i == 0:
            count_0 += 1
        else:
            count_1 += 1
            n -= count_0 // 3
            count_0 = 0
    if count_0 != 0:
        n -= count_0 // 3

    if count_1 == 0:
        n = n - len(flowerbed) // 2

    if n <= 0:
        return True
    else:
        return False


if __name__ == '__main__':
    case =  [1,0,1,0,1,0,1]
    ans = canPlaceFlowers(case, 1)
    print(ans)
    