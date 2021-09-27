from node import DNode

class Queue(object):

    # initializer
    def __init__(self):
        self._head = None
        self._tail = None
        self._num = 0
    
    # insert method
    def enqueue(self, value):
        new = DNode(value)
        if not self._head:
            self._head = new
            self._tail = new
        else:
            if self._tail:
                self._tail._link = new
                new._prev = self._tail
            self._tail = new
        self._num += 1

    # delete method
    def dequeue(self):
        if self._head:
            self._head._link._prev = None
            value = self._head._value
            self._head = self._head._link
            self._num -= 1
            return value
        else:
            print("There's no node to delete it")

    # checking empty
    def is_empty(self):
        return not bool(self._head)
    
    # checking size
    def size(self):
        return self._num

    # return head value
    def peek(self):
        return self._head._value

    # show queue's current state
    def show(self):
        temp = self._head
        while temp:
            print(temp._value, end=" ")
            temp = temp._link
        print()