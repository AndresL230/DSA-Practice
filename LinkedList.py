class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def append(self, node):
        