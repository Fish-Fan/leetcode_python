class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    newHead = Node(x=head.val)

    current = head
    newCurrent = newHead
    tmpMap, i = {}, 0
    nodeMap = {}
    while current.next != None:
        nextNode = current.next
        newCurrent.next = Node(x=nextNode.val)
        nodeMap[i] = newCurrent
        if current.random != None:
            tmpMap[i] = current.random.val
        else:
            tmpMap[i] = None

        current = current.next
        newCurrent = newCurrent.next

    for key, value in tmpMap.items():
        nodeMap[key].random = value

    return newHead


if __name__ == '__main__':
    