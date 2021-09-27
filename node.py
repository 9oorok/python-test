# 단일 연결 리스트를 구현하는 노드
class Node(object):
    def __init__(self, value=None, link=None, prev=None):
        self._value = value
        self._link = link

# 이중 연결 리스트를 구현하는 노드
class DNode(object):
    def __init__(self, value=None, link=None, prev=None):
        self._value = value
        self._link = link
        self._prev = prev