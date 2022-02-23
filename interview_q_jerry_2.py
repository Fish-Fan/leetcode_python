# question link: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/336de20e-3c91-4225-8c52-aee62d4ee648/17901645547556_.pic.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220223T144059Z&X-Amz-Expires=86400&X-Amz-Signature=9f59757e619a4ca8e13a8fd09dcf548292afe4c4fe6632fff69df7f957f8000e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%2217901645547556_.pic.jpg%22&x-id=GetObject
from collections import defaultdict
def solution(s_arr):
    # format input string
    adj_list = defaultdict(list)
    for s in s_arr:
        tmp_arr = s.split(':')
        population, adj_cities = int(tmp_arr[0]), [int(i) for i in tmp_arr[1][1:-1].split(',')]
        adj_list[population].extend(adj_cities)

    # traversing each city and calculate each road traffic volume connected to it, then get the maximum value among those volume
    ans = ""
    for city in adj_list.keys():
        mem, max_traffic_v = {city: True}, 0
        # traversing each road connect to this city
        for neighbor_city in adj_list[city]:
            max_traffic_v = max(max_traffic_v, dfs(neighbor_city, adj_list, mem))
        ans += str(city) + ':' + str(max_traffic_v) + ', '

    return ans[:-1]

def dfs(v, adj_list, mem):
    if v in mem:
        return 0

    # count current city population and mark as visited
    traffic_v = v
    mem[v] = True

    # repeatedly search neighbor city and sum their population to current city
    for nxt in adj_list[v]:
        traffic_v += dfs(nxt, adj_list, mem)
    return traffic_v





if __name__ == '__main__':
    # test case 1
    # s_arr = ['1:[5]', '4:[5]', '3:[5]', '5:[1,4,3,2]', '2:[5,15,7]', '7:[2,8]', '8:[7,38]', '15:[2]', '38:[8]']
    # test case 1
    # s_arr = ['1:[5]', '2:[5,18]', '3:[5,12]', '4:[5]', '5:[1,2,3,4]', '18:[2]', '12:[3]']
    # test case 1
    s_arr = ['1:[5]', '2:[5]', '3:[5]', '4:[5]', '5:[1,2,3,4]']
    ans = solution(s_arr)
    print(ans)