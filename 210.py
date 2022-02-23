def findOrder(numCourses: int, prerequisites):
    n = numCourses
    graph = [[] for i in range(n)]
    visited = [0] * n
    for arr in prerequisites:
        x, y = arr[0], arr[1]
        graph[x].append(y)
    ans = []
    for i in range(n):
        DFS(graph, i, ans, visited)
    return ans


def DFS(graph, j, ans, visited):
    if visited[j] == 1:
        return
    tmp = 0
    for i in graph[j]:
        if visited[i] == 1:
            tmp += 1
    if tmp == len(graph[j]):
        visited[j] = 1
        ans.append(j)
        return

    for i in graph[j]:
        DFS(graph, i, ans, visited)
    ans.append(j)
    visited[j] = 1

if __name__ == '__main__':
    prerequisites = [[1,2],[2,3],[2,4],[3,4]]
    numcourse = 5
    ans = findOrder(numcourse, prerequisites)
    print(ans)