import unittest
from os import listdir
from os.path import isfile, join
from collectionsUtils import defaultdict
from collections import deque
from TreeNode import TreeNode, deserialize
import heapq
import bisect

import re
class UnitTestDemo(unittest.TestCase):
    def testStringFind(self):
        s = 'root/a 1.txt(abcd) 2.txt(efgh)'
        re_search_grounp = re.search('(.*)', s, re.IGNORECASE)
        if re_search_grounp:
            print(re_search_grounp.group(1))

    def testDefaultDict(self):
        arr = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        d = defaultdict(list)
        for item in arr:
            d[item[0]].append(item[1])
        print(d)

    def testSort(self):
        arr = [1,3,2,4]
        arr.sort(reverse=True)
        print(arr)

    def testDefaultDictDque(self):
        arr = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        d = defaultdict(deque)
        for item in arr:
            d[item[0]].append(item[1])
        print(d)

    def testStrMultiply(self):
        s = 'a'
        print(s * 3)

    def testEmptyArr(self):
        arr = []
        arr += [1]
        print(arr)
    def testIsDigital(self):
        print('1'.isdigit())

    def testIntersection(self):
        list1 = [(1,2), (3,4), (5,6)]
        list2 = [(3,4), (5,6), (7,8)]
        ans = list(set(list1).intersection(set(list2)))
        print(ans)

    def testAnyLambda(self):
        arr = [1,2,3]
        result = list(filter(lambda x: x==2, arr))
        print(result)

    def testReverseForloop(self):
        for i in range(10,0,-1):
            print(i)

    def testCreateTwoDimentioanlArray(self):
        arr = [[False for i in range(5)] for j in range(4)]
        print(arr)

    def testFloatInf(self):
        print(1 > float('inf'))
        print(1 < float('-inf'))
        print(1 < float('inf'))
        print(1 > float('-inf'))

    def testLevelTraversalTree(self):
        root = deserialize("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16")
        # root = deserialize('5,4,8,11,null,13,4,7,2,null,null,5,1')
        # root = deserialize('1,null,2,null,3,null,4,null,5,null,6')
        arr, ans = [root], []
        self.dfslevel(arr, ans)
        s = ",".join(ans)[:-1]
        print(s)

    def dfslevel(self, arr, ans):
        if arr:
            if all(item == None for item in arr):
                return
            for node in arr:
                if node:
                    ans.append(str(node.val))
                else:
                    ans.append('null')
            tmp = []
            for i in range(len(arr)):
                node = arr[i]
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)
            arr = tmp[:]
            self.dfslevel(arr, ans)

    def testReverstr(self):
        s = '123'
        print(s[::-1])


    def testCset(self):
        words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # adj = {}
        # adj['A'] = {'C', 'B'}
        # adj['B'] = {'C'}
        # adj['C'] = {}
        visited = {}
        def dfs(node, path, visited):
            if node:
                if node in visited:
                    return
                visited[node] = True
                directions = adj[node]
                for d in directions:
                    dfs(d, path, visited)
                path.append(node)
        path = []
        for key in adj.keys():
            dfs(key, path, visited)
            break
        print(path)

    def testCset1(self):
        tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        graph = defaultdict(list)
        for arr in tickets:
            graph[arr[0]].append(arr[1])

    def testArrDelete(self):
        arr = [1, 2, 3]
        for i, v in enumerate(arr):
            print(v)
            arr.pop(i)

    def testHeapq(self):
        arr = []
        heapq.heappush(arr, (1, 2, 1))
        heapq.heappush(arr, (1, 2, 2))
        heapq.heappush(arr, (1, 2, 3))
        heapq.heappush(arr, (2, 1))
        heapq.heappush(arr, (2, 5))
        heapq.heappush(arr, (3, 1))

        while arr:
            print(heapq.heappop(arr))

    def testMapFunc(self):
        numbers = [1,2,3,4]
        numbers_1 = numbers[:-1]
        numbers_2 = numbers[1:]
        result = map(lambda x,y:x+y, numbers_1, numbers_2)
        print(list(result))

    def testStr(self):
        print('0' < '9')

    def testAAA(self):
        s = '1 box has 3 blue 4 red 6 green and 12 yellow marbles'
        pre_num = '-1'
        for cha in s:
            if '0' <= cha <= '9':
                if cha > pre_num:
                    pre_num = cha
                else:
                    return False
        return True

    def testBitWise(self):
        a, b = 3, 5
        print(a | b)

    def testBisection(self):
        arr = [1,2,2,3,3,5,6,7,7,8]
        i = self.index(arr, 2)
        print(arr[i])
        i = self.find_le(arr, 3)
        print(arr[i])

    def index(self, arr, x):
        # locate the leftmost value exactly to equal to x
        i = bisect.bisect_left(arr, x)
        if i != len(arr) and arr[i] == x:
            return i

    def find_lt(self, arr, x):
        # find rightmost value less than x
        i = bisect.bisect_left(arr, x)
        if i-1 != len(arr):
            return i-1

    def find_le(self, arr, x):
        # find rightmost value less than or equal to x
        i = bisect.bisect_right(arr, x)
        return i-1

    def find_gt(self, arr, x):
        # find leftmost value greater than x
        i = bisect.bisect_right(arr, x)
        return i

    def find_ge(self, arr, x):
        # find leftmost value greater or equal than x
        i = bisect.bisect_left(arr, x)
        return i

    def test_merge_sort(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        print(self.merge_partition(nums))

    def merge_partition(self, arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left_arr = self.merge_partition(arr[:mid])
        right_arr = self.merge_partition(arr[mid:])
        return self.merge(self.merge_partition(left_arr), self.merge_partition(right_arr))

    def merge(self, left_arr, right_arr):
        arr = []
        i, j = 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr.append(left_arr[i])
                i += 1
            else:
                arr.append(right_arr[j])
                j += 1
        while i < len(left_arr):
            arr.append(left_arr[i])
            i += 1
        while j < len(right_arr):
            arr.append(right_arr[j])
            j += 1
        return arr

    def testZipBuiltInFunc(self):
        s_arr = ["ac","aba","zc","zb"]
        for first_word, second_word in zip(s_arr, s_arr[1:]):
            for a, b in zip(first_word, second_word):
                print(a)
                print(b)
            print('-----')




