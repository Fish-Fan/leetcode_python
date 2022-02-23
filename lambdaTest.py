from functools import cmp_to_key

if __name__ == '__main__':
    fun1 = lambda a: a+10
    print(fun1(5))

    arr = [4,3,2,1]
    ansArr = list(map(fun1, arr))
    print(ansArr)

    cmop = lambda a,b: 1 if a>b else -1
    ansArr = sorted(arr, key=cmp_to_key(cmop))
    print(ansArr)

    arr = [1,5,9,1,5,9]
    arr_slice = arr[:3]
    arr_slice[0] = 9
    arr_slice[1] = 5
    arr_slice[2] = 1
    print(arr)
