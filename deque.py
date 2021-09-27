from node import DNode
from queue import Queue

# Queue 클래스를 상속받아서 구현
class Deque(Queue):

    # second insert method
    def enqueue_head(self, value):
        self._head = DNode(value, self._head)
        self._head._link._prev = self._head
        self._num += 1
    
    # second delete method
    def dequeue_tail(self):
        if self._num > 0 and self._tail:
            rear = self._tail
            self._tail = rear._prev
            self._tail._link = None
            self._num -= 1
            return rear._value
        else:
            print("There's no node to delete it")