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

    def insBack(self, val):
        node = Node(val)

        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def insFront(self, val):
        node = Node(val)
        
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()