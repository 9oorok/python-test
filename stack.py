from node import Node

class Stack(object):

    # initializer
    def __init__(self):
        self._head = None
        self._num = 0

    # insert method
    def push(self, value):
        self._head = Node(value, self._head)
        self._num += 1

    # delete method
    def pop(self):
        if self._num > 0 and self._head:
            top = self._head
            self._head = top._link
            self._num -= 1
            return top._value
        else:
            print("There's no node to pop it")

    # checking empty
    def is_empty(self):
        return not bool(self._head)

    # checking size
    def size(self):
        return self._num
    
    # return top value
    def peek(self):
        if self._num > 0 and self._head:
            return self._head._value
        else:
            print("There's no node to show you")

    # show stack's current state
    def show(self):
        top = self._head
        while top:
            print(top._value, end=' ')
            top = top._link
        print()