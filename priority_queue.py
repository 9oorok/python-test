# heapq 모듈을 사용해서 우선순위 큐를 구현
import heapq

class Node(object):
    def __init__(self, value=None):
        self.value = value

# 최소 힙 기반
class PriorityQueue(object):

    # initializer
    def __init__(self):
        self._queue = []
        self._index = 0

    # insert method
    def push(self, value):
        heapq.heappush(self._queue, value)
        self._index += 1
    
    # delete method
    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)
        else:
            print("There's no node to delete it")

    # show queue's current state
    def show(self):
        print(self._queue)