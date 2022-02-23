import GraphNode as Node


def cloneGraph( node: 'Node') -> 'Node':
    pathMap = {}
    DFS(node, pathMap)

    ansNode, i = None, 0
    nodeMap = {}
    for key in pathMap.keys():
        newNode = Node.Node(key)
        nodeMap[key] = newNode
    for key in nodeMap.keys():
        newNode = nodeMap.get(key)
        neighborsArr = pathMap.get(key)
        tmpArr = []
        for v in neighborsArr:
            tmpArr.append(nodeMap.get(v))
        newNode.neighbors = tmpArr
        if i == 0:
            ansNode = newNode
        i += 1
    return ansNode


def DFS(node, pathMap):
    if node.val in pathMap:
        return
    neighborArr = []
    for i in node.neighbors:
        neighborArr.append(i.val)
    pathMap[node.val] = neighborArr
    DFS(node.neighbors[0], pathMap)
    DFS(node.neighbors[1], pathMap)

if __name__ == '__main__':
    node1 = Node.Node(1)
    node2 = Node.Node(2)
    node3 = Node.Node(3)
    node4 = Node.Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    ans = cloneGraph(node1)
    print(ans)