from queue import PriorityQueue

if __name__ == '__main__':
    q = PriorityQueue()
    q.put((-12,12))
    q.put((-14,14))
    q.put((-1,1))
    q.put((-3,3))

    while not q.empty():
        print(q.get())