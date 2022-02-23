from collectionsUtils import defaultdict


def findItinerary(tickets):
    targets = defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []

    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)

    visit('JFK')
    return route[::-1]


if __name__ == '__main__':
    arr = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    ans = findItinerary(arr)
    print(ans)